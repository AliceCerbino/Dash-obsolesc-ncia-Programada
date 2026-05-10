# =============================================================================
# EcoDurable — Coleta e Tratamento de Dados
# Base: What a Waste Global Database (Banco Mundial)
# Autora: Alice Cerbino Soares
# =============================================================================

import pandas as pd
import numpy as np

# =============================================================================
# 1. CARREGAMENTO DA BASE
# =============================================================================

# A base What a Waste Global Database foi obtida diretamente pelo portal
# do Banco Mundial em: https://datacatalog.worldbank.org/dataset/what-waste-global-database
# e importada localmente no formato .xlsx

df = pd.read_excel("what_a_waste.xlsx")

print("Shape original:", df.shape)
print("\nColunas disponíveis:")
print(df.columns.tolist())

# =============================================================================
# 2. ANÁLISE EXPLORATÓRIA INICIAL
# =============================================================================

print("\n--- Primeiras linhas ---")
print(df.head())

print("\n--- Tipos de dados ---")
print(df.dtypes)

print("\n--- Valores nulos por coluna ---")
print(df.isnull().sum())

print("\n--- Estatísticas descritivas ---")
print(df.describe())

# =============================================================================
# 3. SELEÇÃO DOS ATRIBUTOS RELEVANTES
# =============================================================================

# Seleção das colunas com maior aderência ao tema de obsolescência programada
colunas_selecionadas = [
    "country_name",
    "region_id",
    "income_id",
    "total_msw_total_msw_generated_tons_year",
    "msw_total_msw_generated_kg_per_cap_per_day",
    "composition_plastic_percent",
    "composition_metal_percent",
    "waste_collection_coverage_total_percent_of_waste",
    "waste_treatment_recycling_percent",
    "waste_treatment_open_dumpsite_percent",
    "total_msw_total_msw_generated_tons_year_projected_2030",
    "total_msw_total_msw_generated_tons_year_projected_2040",
    "total_msw_total_msw_generated_tons_year_projected_2050",
]

df = df[colunas_selecionadas].copy()

print("\nShape após seleção de atributos:", df.shape)

# =============================================================================
# 4. LIMPEZA E TRATAMENTO DOS DADOS
# =============================================================================

# 4.1 Remoção de linhas sem país definido
df = df.dropna(subset=["country_name"])
print("\nLinhas após remover países nulos:", len(df))

# 4.2 Padronização dos nomes de países (strip de espaços extras)
df["country_name"] = df["country_name"].str.strip()

# 4.3 Preenchimento de valores nulos em percentuais com a mediana por região
# Evita distorção por outliers em regiões com poucos dados
colunas_percentuais = [
    "composition_plastic_percent",
    "composition_metal_percent",
    "waste_collection_coverage_total_percent_of_waste",
    "waste_treatment_recycling_percent",
    "waste_treatment_open_dumpsite_percent",
]

for col in colunas_percentuais:
    mediana_por_regiao = df.groupby("region_id")[col].transform("median")
    df[col] = df[col].fillna(mediana_por_regiao)

# 4.4 Preenchimento de valores nulos em toneladas com 0
# Países sem dado de geração registrado assumem volume 0
colunas_toneladas = [
    "total_msw_total_msw_generated_tons_year",
    "total_msw_total_msw_generated_tons_year_projected_2030",
    "total_msw_total_msw_generated_tons_year_projected_2040",
    "total_msw_total_msw_generated_tons_year_projected_2050",
]

df[colunas_toneladas] = df[colunas_toneladas].fillna(0)

# 4.5 Verificação de percentuais fora do intervalo [0, 100]
for col in colunas_percentuais:
    invalidos = df[(df[col] < 0) | (df[col] > 100)]
    if not invalidos.empty:
        print(f"\nAtenção: valores fora do intervalo em {col}:")
        print(invalidos[["country_name", col]])
        df[col] = df[col].clip(0, 100)

print("\nValores nulos após tratamento:")
print(df.isnull().sum())

# =============================================================================
# 5. CRIAÇÃO DE MÉTRICAS DERIVADAS
# =============================================================================

# 5.1 Índice de Risco por Obsolescência Programada
# Combina composição de plástico e metal com baixa reciclagem
# Quanto maior o índice, maior o risco de acúmulo de resíduos
# relacionados ao descarte precoce de produtos
df["risco_obsolescencia"] = (
    df["composition_plastic_percent"]
    + df["composition_metal_percent"]
    - df["waste_treatment_recycling_percent"]
)

# 5.2 Lixo Não Reciclado
# Percentual de resíduos que não passa por nenhum processo de recuperação
df["lixo_nao_reciclado_percent"] = 100 - df["waste_treatment_recycling_percent"]

# 5.3 Crescimento Projetado até 2050
# Volume absoluto de resíduos adicionais esperados até 2050
df["crescimento_2050_tons"] = (
    df["total_msw_total_msw_generated_tons_year_projected_2050"]
    - df["total_msw_total_msw_generated_tons_year"]
)

print("\n--- Métricas derivadas (amostra) ---")
print(df[["country_name", "risco_obsolescencia", "lixo_nao_reciclado_percent", "crescimento_2050_tons"]].head(10))

# =============================================================================
# 6. TRANSFORMAÇÃO PARA SÉRIE TEMPORAL (UNPIVOT / MELT)
# =============================================================================

# A base original armazena as projeções em colunas separadas (formato wide).
# Para construção do gráfico de linhas temporal, os dados precisam estar
# no formato long — cada ano como uma linha distinta por país.

df_projecao = df[
    [
        "country_name",
        "region_id",
        "income_id",
        "total_msw_total_msw_generated_tons_year",
        "total_msw_total_msw_generated_tons_year_projected_2030",
        "total_msw_total_msw_generated_tons_year_projected_2040",
        "total_msw_total_msw_generated_tons_year_projected_2050",
    ]
].copy()

# Renomeia colunas para anos antes do melt
df_projecao = df_projecao.rename(columns={
    "total_msw_total_msw_generated_tons_year": "2020",
    "total_msw_total_msw_generated_tons_year_projected_2030": "2030",
    "total_msw_total_msw_generated_tons_year_projected_2040": "2040",
    "total_msw_total_msw_generated_tons_year_projected_2050": "2050",
})

# Aplica o melt (equivalente ao Unpivot do Power Query)
df_projecao_long = df_projecao.melt(
    id_vars=["country_name", "region_id", "income_id"],
    value_vars=["2020", "2030", "2040", "2050"],
    var_name="ano",
    value_name="total_toneladas",
)

# Converte ano para inteiro
df_projecao_long["ano"] = df_projecao_long["ano"].astype(int)

print("\n--- Dados no formato long (projeção temporal) ---")
print(df_projecao_long.head(12))
print("\nShape formato long:", df_projecao_long.shape)

# =============================================================================
# 7. ANÁLISE REGIONAL — FILTRO AMÉRICA LATINA
# =============================================================================

# Filtro para a página América Latina View do dashboard
# Código LAC = Latin America & Caribbean (classificação Banco Mundial)
df_lac = df[df["region_id"] == "LAC"].copy()

print(f"\nPaíses na região LAC: {len(df_lac)}")
print(df_lac["country_name"].tolist())

print("\n--- Média dos indicadores na América Latina ---")
print(df_lac[colunas_percentuais + ["risco_obsolescencia"]].mean().round(2))

# =============================================================================
# 8. EXPORTAÇÃO DOS DADOS TRATADOS
# =============================================================================

# Base principal tratada — importada no Power BI Online
df.to_csv("whatawaste_tratado.csv", index=False, encoding="utf-8-sig")
print("\nArquivo exportado: whatawaste_tratado.csv")

# Base em formato long para o gráfico de projeção temporal
df_projecao_long.to_csv("whatawaste_projecao_long.csv", index=False, encoding="utf-8-sig")
print("Arquivo exportado: whatawaste_projecao_long.csv")

# Base filtrada América Latina
df_lac.to_csv("whatawaste_lac.csv", index=False, encoding="utf-8-sig")
print("Arquivo exportado: whatawaste_lac.csv")

print("\n✅ Pipeline de tratamento concluído com sucesso.")
