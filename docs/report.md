# EcoDurable: Dashboard Obsolescência Programada 


**Alice Cerbino Soares, alice.cerbino.me@gmail.com**

---

Professor:

** Prof. Jose Laerte Pieres Xavier Junior **

---

_Curso de Ciência de Dados, Unidade Praça da Liberdade_

_Instituto de Informática e Ciências Exatas – Pontifícia Universidade de Minas Gerais (PUC MINAS), Belo Horizonte – MG – Brasil_

---

_**Resumo**. Escrever aqui o resumo. O resumo deve contextualizar rapidamente o trabalho, descrever seu objetivo e, ao final, 
mostrar algum resultado relevante do trabalho (até 10 linhas)._

---


## Introdução
###    Contextualização

O projeto EcoDurable surge como uma resposta tecnológica ao desafio imposto pela obsolescência programada, prática industrial que limita deliberadamente a vida útil de produtos para forçar ciclos de consumo mais curtos. Este fenômeno é um dos principais vetores do crescimento exponencial de resíduos eletroeletrônicos, impactando diretamente a sustentabilidade ambiental e o direito do consumidor.

Alinhado ao Objetivo de Desenvolvimento Sustentável 12 (Consumo e Produção Responsáveis) da Agenda 2030 da ONU, esta aplicação propõe a criação de um ecossistema de dados transparente. Através de um Dashboard de Análise de Durabilidade, o software processa registros de falhas e reclamações provenientes de bases de dados públicas para quantificar a confiabilidade de dispositivos e fabricantes.

Sob a ótica da Engenharia de Software, o projeto aplica conceitos de arquitetura cliente-servidor, modelagem relacional e gerenciamento ágil para transformar dados brutos em métricas acionáveis, auxiliando consumidores em decisões de compra mais conscientes e fornecendo subsídios para o monitoramento de práticas de mercado predatórias.

###    Problema

O descarte precoce de produtos devido à baixa durabilidade gera um volume alarmante de resíduos sólidos. Consumidores muitas vezes carecem de dados consolidados sobre quais marcas e modelos apresentam defeitos em curto espaço de tempo. Este dashboard visa transformar registros de reclamações em índices de durabilidade e reparabilidade.

###    Objetivo geral

Este projeto aborda o ODS 12, especificamente a meta de reduzir a geração de resíduos. O objetivo é fornecer uma ferramenta de transparência que utilize dados de reclamações públicas para medir a durabilidade real de produtos eletrônicos e eletrodomésticos, combatendo a obsolescência programada.

###   Tipo de Solução 

A solução é um Dashboard de Dados com arquitetura dividida em:

> Backend: API para processamento, filtragem e agregação de grandes volumes de dados.

> Banco de Dados: Persistência de dados limpos de fontes como o Consumidor.gov.br.

> Frontend: Interface analítica com gráficos de desempenho e rankings de fabricantes.> 


###    Justificativas

A escolha pelo desenvolvimento do EcoDurable fundamenta-se na necessidade de instrumentalizar o consumidor frente à crescente opacidade do ciclo de vida de produtos tecnológicos. Embora a Política Nacional de Resíduos Sólidos e o Código de Defesa do Consumidor ofereçam amparo legal, a prática da obsolescência programada persiste devido à dispersão de dados técnicos e de performance real.

Do ponto de vista técnico e de Engenharia de Software, o desenvolvimento desta solução justifica-se pela complexidade de tratamento de dados heterogêneos. A aplicação de um dashboard com suporte de backend e banco de dados é essencial para:

- Agregação de Valor: Transformar dados brutos de reclamações em indicadores estatísticos (como o índice de morte prematura), algo que páginas estáticas não comportam.

- Escalabilidade e Persistência: Permitir o armazenamento histórico de falhas, possibilitando a análise de tendências de mercado ao longo de diferentes sprints de dados.

- Rigor Metodológico: Aplicar padrões de projeto e testes de software para garantir que a métrica de durabilidade exibida seja íntegra e auditável.

- Socialmente, o projeto contribui para a Economia Circular, ao incentivar a escolha por produtos mais duráveis e de fácil reparação, reduzindo o impacto ambiental e os custos financeiros derivados do descarte precoce. 

##    Público alvo

O EcoDurable foi projetado para atender diferentes camadas da sociedade interessadas na durabilidade de bens de consumo e na sustentabilidade:
- Consumidores Finais (B2C): Pessoas físicas que buscam informações técnicas e históricas sobre a vida útil de eletroeletrônicos antes de realizar uma compra, visando o melhor custo-benefício e a redução do descarte precoce.

- Órgãos de Defesa do Consumidor e ONGs: Entidades (como o Procon ou institutos de defesa do consumidor) que necessitam de dados consolidados para identificar padrões de comportamento predatório por parte de fabricantes e embasar ações de fiscalização ou campanhas de conscientização.

- Pesquisadores e Gestores Ambientais: Profissionais que analisam o ciclo de vida dos produtos e o impacto da obsolescência programada na geração de resíduos sólidos (e-waste), utilizando o dashboard como ferramenta de suporte para estudos sobre economia circular.

### Diagrama de Caso de Uso

<img width="1364" height="239" alt="Diagrama Caso de Uso" src="https://github.com/user-attachments/assets/005f20fa-ed91-4c17-af5f-6ffa9d01dfb1" />

## Requisitos 

### Requisitos Funcionais
RF01 – Visualizar mapa mundial.
RF02 – Visualizar mapa da América Latina.
RF03 – Visualizar mapa do Brasil.
RF04 – Selecionar indicadores.
RF05 – Exibir gráficos relacionados aos dados.
RF06 – Filtrar informações por região.

### Requisitos Não Funcionais
RNF01 – Interface responsiva.
RNF02 – Tempo de carregamento inferior a 5 segundos.
RNF03 – Dados armazenados em formato CSV/JSON.
RNF04 – Aplicação executável via navegador.

## Arquitetura

### Escolhas de Tecnologias

As tecnologias selecionadas para este projeto visam um equilíbrio estratégico entre estabilidade, ecossistema e facilidade de integração, permitindo que o sistema seja sustentável a longo prazo.

Para o Backend Core, optamos pelo Java 17 acompanhado do framework Spring Boot. Esta escolha baseia-se na robustez que o ecossistema Java oferece, especialmente no que tange à injeção de dependência. Isso é fundamental para manter nossos componentes desacoplados, além de oferecer tipagem forte, o que é crucial para garantir a integridade das regras de negócio complexas que o projeto exige.

No que se refere à Persistência de Dados, utilizamos o PostgreSQL. A decisão foi tomada priorizando a conformidade com as propriedades ACID (Atomicidade, Consistência, Isolamento e Durabilidade), que são essenciais para dados de conformidade e auditoria. Além disso, o PostgreSQL possui um suporte excelente para consultas analíticas complexas, o que facilita a geração de métricas de durabilidade.

Para a Integração, adotamos uma Arquitetura de Adaptadores. Este padrão permite isolar as instabilidades inerentes a APIs externas — como fontes governamentais ou dados públicos — dentro de módulos específicos. Desta forma, protegemos o restante do sistema contra mudanças bruscas nessas fontes externas.

Por fim, delegamos a Visualização ao Power BI. Ao utilizar uma ferramenta dedicada ao Business Intelligence, removemos a sobrecarga de renderização de gráficos complexos do backend. Isso nos permite focar o desenvolvimento do nosso sistema exclusivamente no processamento, tratamento e lógica de análise de dados, delegando a apresentação interativa a uma plataforma otimizada para esse fim.

### Projeto de Arquitetura

O EcoDurable System é uma plataforma analítica projetada para consolidar, processar e visualizar métricas de durabilidade e obsolescência programada de produtos. O sistema atua como uma ponte entre dados públicos brutos e decisões informadas, servindo desde consumidores finais até órgãos de fiscalização e pesquisadores de mercado.

Para garantir clareza, a arquitetura foi desenhada utilizando o Modelo C4, permitindo uma decomposição hierárquica ("zoom") que separa as preocupações de negócio das preocupações técnicas:

> Nível 1 (Contexto): Define o papel do sistema no ecossistema (usuários vs. fontes de dados externas).

> Nível 2 (Containers): Define a "infraestrutura física" (onde o código vive).

> Nível 3 (Componentes): Define a "organização interna" do Backend (módulos lógicos).

> Nível 4 (Código): Define o "contrato" de implementação (interfaces e classes).

#### System Context

<img width="1920" height="1080" alt="Model C4 - Context" src="https://github.com/user-attachments/assets/7ceb1e72-c567-4537-941e-9c5ff836ea9e" />

O sistema não opera em isolamento. Ele atua como um hub central que:

- Ingere: Coleta dados de fontes externas (governamentais, índices públicos).

- Processa: Transforma esses dados em inteligência (métricas de falha, vida útil).

- Distribui: Fornece relatórios via E-mail e Dashboards interativos (Power BI), com foco no Órgão Fiscalizador.

#### Container

<img width="1920" height="1080" alt="Model C4 - Container" src="https://github.com/user-attachments/assets/9aadefbc-4655-44dd-a796-404926588e20" />

Nossa arquitetura de containers é baseada em desacoplamento funcional:

- Frontend (Power BI): Focado exclusivamente em UX e visualização, mantendo a camada de apresentação independente da lógica de cálculo.

- Backend (API REST): O orquestrador central. Gerencia toda a lógica de negócio, autenticação (Spring Security) e roteamento.

- ETL (Data Processing Service): Um container dedicado à ingestão e limpeza. Ao separar o ETL do Backend principal, garantimos que processos de ingestão de alto volume não impactem a performance da API.

- Storage & Database (PostgreSQL): Separação clara entre o "Raw Data" (Object Storage - dados brutos) e o "Processed Data" (Database - métricas estruturadas e históricas).

#### Component

<img width="1920" height="1080" alt="Model C4 - Component" src="https://github.com/user-attachments/assets/e712de74-e0cc-47fd-8445-12668e6ea16b" />

Dentro do Backend, a organização segue o padrão de Componentes Spring:

- API Controller: Porta de entrada e gestão de segurança.

- Serviços de Domínio (Filtering Engine, Ranking Engine, Data Processing): Onde reside a inteligência. O Ranking Engine não acessa banco de dados diretamente; ele solicita dados processados, mantendo a responsabilidade limitada.

- Data Repository (JPA): A única camada com permissão de manipulação direta de banco, garantindo consistência.

#### Code

<img width="1920" height="1080" alt="Model C4 - Code" src="https://github.com/user-attachments/assets/96971afa-f292-47c8-8cae-787e6b2f725b" />

Como visto no diagrama de código, utilizamos a interface IDataSourceAdapter. Isso significa que, independentemente de onde o dado venha (Governo, API Pública, Arquivo local), o restante do sistema (Ranking, Processamento) enxerga apenas o contrato (fetchData()). Isso blinda o código contra mudanças externas. 

#### Arquitetura Geral em Zoom

<img width="1920" height="1080" alt="Model C4 - Visão Geral do Zoom" src="https://github.com/user-attachments/assets/bb51af35-3cc3-4af6-909c-fa2db0a7638e" />

### Justificativa da Arquitetura

A arquitetura adotada para o sistema EcoDurable fundamenta-se em princípios de design de software que visam mitigar a fragilidade sistêmica e promover a sustentabilidade do código a longo prazo. A estrutura proposta não é apenas uma organização lógica, mas uma estratégia deliberada para endereçar desafios fundamentais em sistemas de processamento de dados. A seguir, detalham-se os pilares que conferem resiliência, escalabilidade e manutenibilidade ao projeto.

#### Mitigação do Acoplamento e Resiliência a Mudanças
   
A volatilidade de fontes de dados externas representa um risco constante para sistemas que dependem de integração via APIs de terceiros. Em arquiteturas monolíticas tradicionais, a lógica de negócio é frequentemente contaminada por detalhes técnicos de acesso a dados, o que gera um alto grau de acoplamento.

O projeto EcoDurable endereça este desafio através da aplicação do padrão de projeto Adapter, combinado com o Princípio da Inversão de Dependência (DIP). Ao estabelecer uma interface contratual — IDataSourceAdapter — entre o serviço de domínio (RankingService) e os fornecedores de dados, o sistema torna-se agnóstico à origem da informação. Consequentemente, caso ocorram alterações estruturais na API do fornecedor, o impacto é restrito estritamente à classe que implementa o adaptador específico. A lógica de negócio permanece intacta, protegida por uma camada de abstração que isola a volatilidade externa, garantindo a continuidade operacional e reduzindo a necessidade de regressões em componentes críticos do sistema.

#### Otimização de Recursos e Escalabilidade Independente

A heterogeneidade das cargas de trabalho é um fator determinante para a eficiência computacional. O sistema distingue claramente entre dois perfis de processamento: a ingestão de dados brutos (ETL - Extract, Transform, Load) e a disponibilização de informações via API (Backend).

Ao estratificar o processo de ETL em um container isolado e independente do serviço de API, a arquitetura permite uma gestão de recursos granular. Operações de processamento de dados massivos, que demandam alta capacidade de CPU e memória, não competem diretamente com os recursos necessários para a baixa latência de requisições HTTP do Frontend. Esta separação possibilita a alocação de infraestrutura específica para cada subdomínio — realizando o scale-up ou scale-out do processamento de dados sem onerar a disponibilidade do serviço de consulta do usuário. Esta abordagem não apenas otimiza o custo operacional (Cloud Spending), mas também elimina estrangulamentos de desempenho (bottlenecks) que ocorreriam em um ambiente unificado.

#### Rigor Metodológico e Testabilidade

A testabilidade é um indicador direto da maturidade de uma arquitetura. A arquitetura em camadas aqui proposta favorece a adoção de estratégias de Unit Testing de alta eficácia, ao promover a separação de responsabilidades (Separation of Concerns).

Pela estrutura modular, cada componente pode ser validado de forma isolada, sem dependências externas. O RankingService, por exemplo, pode ser submetido a testes determinísticos mediante a injeção de mocks ou stubs que implementam a interface de dados, simulando diferentes cenários (sucesso, falha ou dados corrompidos) sem a necessidade de uma conexão real com o banco de dados ou ambiente de produção. Este isolamento metodológico reduz a complexidade dos testes, acelera os ciclos de feedback no desenvolvimento (Continuous Integration) e assegura que a integridade dos algoritmos de cálculo de durabilidade seja mantida a cada nova alteração, mitigando o risco de introdução de efeitos colaterais indesejados.

## 3.1 Análise Exploratória dos Dados

### 3.1.1 Descrição da Base de Dados

A base de dados utilizada neste trabalho é a *What a Waste Global Database*, disponibilizada publicamente pelo Banco Mundial. Trata-se de um repositório de dados secundários que consolida informações sobre geração e gestão de resíduos sólidos urbanos de países ao redor do mundo, coletadas a partir de relatórios governamentais, estudos regionais e levantamentos de campo realizados por especialistas do setor.

A base é composta por registros em nível de país, abrangendo nações de todas as regiões geográficas e faixas de renda, organizadas segundo a classificação do próprio Banco Mundial — baixa renda (LIC), renda média-baixa (LMC), renda média-alta (UMC) e alta renda (HIC). Cada registro agrega atributos quantitativos relacionados à geração, composição e tratamento dos resíduos, além de projeções de geração para os anos de 2030, 2040 e 2050.

### 3.1.2 Seleção e Justificativa dos Atributos

Dos atributos disponíveis na base, foram selecionados aqueles com maior aderência ao fenômeno da obsolescência programada e à geração de resíduos associada ao descarte precoce de produtos. O quadro a seguir apresenta os atributos utilizados e suas respectivas justificativas:

| Atributo | Descrição | Justificativa |
|---|---|---|
| `total_msw_total_msw_generated_tons_year` | Total de resíduos sólidos urbanos gerados por ano (toneladas) | Indicador central de volume de descarte por país |
| `msw_total_msw_generated_kg_per_cap_per_day` | Geração per capita diária (kg/pessoa/dia) | Permite comparações independentes de tamanho populacional |
| `composition_plastic_percent` | Percentual de plástico na composição dos resíduos | Proxy do descarte de produtos com componentes plásticos, diretamente relacionados a eletroeletrônicos |
| `composition_metal_percent` | Percentual de metal na composição dos resíduos | Proxy do descarte de componentes metálicos de dispositivos eletrônicos |
| `waste_treatment_recycling_percent` | Percentual de resíduos destinados à reciclagem | Indicador da capacidade de recuperação de materiais |
| `waste_treatment_open_dumpsite_percent` | Percentual destinado a lixões a céu aberto | Indicador de inadequação no tratamento de resíduos |
| `waste_collection_coverage_total_percent_of_waste` | Cobertura total do serviço de coleta de resíduos | Indicador de infraestrutura de gestão de resíduos |
| `total_msw_total_msw_generated_tons_year_projected_2030` | Projeção de geração para 2030 (toneladas) | Permite análise de tendência futura do descarte |
| `total_msw_total_msw_generated_tons_year_projected_2040` | Projeção de geração para 2040 (toneladas) | Permite análise de tendência futura do descarte |
| `total_msw_total_msw_generated_tons_year_projected_2050` | Projeção de geração para 2050 (toneladas) | Cenário de longo prazo para impacto ambiental |
| `region_id` | Identificador da região geográfica | Permite segmentação e análise regional |
| `income_id` | Classificação de renda do país | Permite análise socioeconômica comparativa |
| `country_name` | Nome do país | Atributo de geolocalização para visualizações em mapa |

## 3.2 Preparação dos Dados

### 3.2.1 Importação e Conexão com a Base

A base *What a Waste Global Database* foi importada diretamente no Microsoft Power BI Online no formato de planilha estruturada. Após a importação, os dados foram carregados no ambiente do Power Query Editor, ferramenta nativa do Power BI responsável pelo tratamento e transformação de dados antes de sua disponibilização para os visuais do dashboard.

### 3.2.2 Transformação das Colunas de Projeção

Um dos principais desafios identificados na estrutura original da base foi a disposição das projeções de geração de resíduos. Os valores referentes aos anos de 2030, 2040 e 2050 estavam armazenados como colunas independentes na mesma linha de cada país, no formato *wide*, conforme ilustrado abaixo:

| País | Toneladas Atual | Projeção 2030 | Projeção 2040 | Projeção 2050 |
|---|---|---|---|---|
| Brasil | 79.000.000 | 95.000.000 | 112.000.000 | 130.000.000 |

Este formato impede a construção de um gráfico de linhas temporal, pois o Power BI requer que os dados estejam no formato *long* — ou seja, cada ano como uma linha distinta. Para solucionar este problema, foi aplicada a operação de **despivotamento** (*Unpivot*) no Power Query, seguindo os passos:

1. Seleção simultânea das quatro colunas de geração (`total_msw_total_msw_generated_tons_year`, `...projected_2030`, `...projected_2040`, `...projected_2050`)
2. Aplicação da operação **"Despivotar Colunas Selecionadas"**
3. Renomeação da coluna `Atributo` para `Ano` e da coluna `Valor` para `Total_Toneladas`
4. Substituição dos valores textuais da coluna `Ano` pelos anos correspondentes: `2020`, `2030`, `2040` e `2050`
5. Conversão da coluna `Ano` para o tipo de dado **Número Inteiro**

Após a transformação, a estrutura resultante permitiu a construção do gráfico de linhas com projeção temporal, com cada ponto representando um ano distinto no eixo horizontal.

### 3.2.3 Criação de Medidas Calculadas (DAX)

Para enriquecer a análise além dos atributos originais da base, foram criadas medidas calculadas utilizando a linguagem DAX (*Data Analysis Expressions*), nativa do Power BI. As medidas desenvolvidas são descritas a seguir.

#### a) Índice de Risco por Obsolescência Programada

Esta medida constitui o principal indicador analítico do dashboard. Combina a composição de materiais associados ao descarte de eletroeletrônicos — plástico e metal — com a capacidade de reciclagem do país, gerando um índice que quanto maior, maior o risco de acúmulo de resíduos relacionados à obsolescência programada:

```dax
Risco_Obsolescencia =
AVERAGE('whatawaste'[composition_plastic_percent])
+ AVERAGE('whatawaste'[composition_metal_percent])
- AVERAGE('whatawaste'[waste_treatment_recycling_percent])
```

A lógica da medida fundamenta-se na premissa de que países com alta concentração de plástico e metal nos resíduos, combinada com baixa taxa de reciclagem, apresentam maior vulnerabilidade ao impacto da obsolescência programada — descartando mais materiais potencialmente recuperáveis sem o devido tratamento.

#### b) Crescimento Projetado até 2050

Esta medida calcula o volume absoluto de resíduos adicionais que serão gerados até 2050 em relação ao cenário atual, fornecendo uma dimensão concreta do impacto futuro:

```dax
Crescimento_2050 =
SUM('whatawaste'[total_msw_total_msw_generated_tons_year_projected_2050])
- SUM('whatawaste'[total_msw_total_msw_generated_tons_year])
```

#### c) Lixo Não Reciclado

Medida que estima o percentual médio de resíduos que não passa por nenhum processo de recuperação, somando o descarte em lixões com demais formas inadequadas de tratamento:

```dax
Lixo_Nao_Reciclado =
100 - AVERAGE('whatawaste'[waste_treatment_recycling_percent])
```

## 3.3 Construção dos Gráficos e Visuais

### 3.3.1 Mapa Coroplético — Distribuição Global de Resíduos

O mapa coroplético foi construído utilizando o visual nativo **Mapa Preenchido** do Power BI. Cada país é colorido em uma escala de gradiente com base no volume total de resíduos gerados anualmente, utilizando a paleta do projeto — do branco (`#ffffff`) ao roxo escuro (`#894b96`). Países com maior geração de resíduos apresentam coloração mais intensa, permitindo uma leitura geográfica imediata da distribuição global do descarte.

- **Campo Localização:** `country_name`
- **Campo Saturação de cor:** `total_msw_total_msw_generated_tons_year`

### 3.3.2 Mapa de Bolhas — Índice de Risco por Obsolescência

O mapa de bolhas foi construído com o visual **Mapa** do Power BI, posicionando cada país como uma bolha cujo tamanho é proporcional ao Índice de Risco por Obsolescência Programada calculado via DAX. A saturação de cor representa o percentual de descarte em lixões a céu aberto, adicionando uma segunda dimensão analítica à visualização.

- **Campo Localização:** `country_name`
- **Campo Tamanho:** `Risco_Obsolescencia`
- **Campo Saturação de cor:** `waste_treatment_open_dumpsite_percent`
- **Campo Dicas de ferramentas:** `waste_treatment_recycling_percent`

### 3.3.3 Gráfico de Rosca — Composição dos Resíduos

O gráfico de rosca apresenta a composição percentual dos resíduos globais, com ênfase nos materiais associados ao descarte de produtos eletroeletrônicos. A visualização evidencia a proporção de plástico e metal em relação ao total de resíduos gerados.

- **Campo Legenda:** categorias de composição (`composition_plastic_percent`, `composition_metal_percent`)
- **Campo Valores:** média de cada categoria
- **Paleta:** tons de roxo (`#894b96`, `#b07cba`, `#d4aede`)

### 3.3.4 Gráfico de Linhas — Projeção de Resíduos até 2050

Construído a partir dos dados transformados pelo despivotamento descrito na seção 3.2.2, o gráfico de linhas representa a evolução projetada da geração global de resíduos nos anos de 2020, 2030, 2040 e 2050. A visualização reforça o caráter prospectivo do dashboard, evidenciando o crescimento contínuo do volume de descarte caso os padrões de consumo e obsolescência se mantenham.

- **Eixo X:** `Ano`
- **Eixo Y:** Soma de `Total_Toneladas`
- **Cor da linha:** `#894b96`

## Resultados

### Resultados obtidos com o modelo 1.

Apresente aqui os resultados obtidos com a indução do modelo 1. 
Apresente uma matriz de confusão quando pertinente. Apresente as medidas de performance
apropriadas para o seu problema. 
Por exemplo, no caso de classificação: precisão, revocação, F-measure, acurácia.

### Interpretação do modelo 1

Apresente os parâmetros do modelo obtido. Tentre mostrar as regras que são utilizadas no
processo de 'raciocínio' (*reasoning*) do sistema inteligente. Utilize medidas como 
o *feature importances* para tentar entender quais atributos o modelo se baseia no
processo de tomada de decisão.


### Resultados obtidos com o modelo 2.

Repita o passo anterior com os resultados do modelo 2.

### Interpretação do modelo 2

Repita o passo anterior com os parâmetros do modelo 2.


## Análise comparativa dos modelos

Discuta sobre as forças e fragilidades de cada modelo. Exemplifique casos em que um
modelo se sairia melhor que o outro. Nesta seção é possível utilizar a sua imaginação
e extrapolar um pouco o que os dados sugerem.


### Distribuição do modelo (opcional)

Tende criar um pacote de distribuição para o modelo construído, para ser aplicado 
em um sistema inteligente.


## 8. Conclusão

Apresente aqui a conclusão do seu trabalho. Discussão dos resultados obtidos no trabalho, 
onde se verifica as observações pessoais de cada aluno.

Uma conclusão deve ter 3 partes:

   * Breve resumo do que foi desenvolvido
	 * Apresenação geral dos resultados obtidos com discussão das vantagens e desvantagens do sistema inteligente
	 * Limitações e possibilidades de melhoria


# REFERÊNCIAS

Como um projeto de sistema inteligente não requer revisão bibliográfica, 
a inclusão das referências não é obrigatória. No entanto, caso você 
tenha utilizado referências na introdução ou deseje 
incluir referências relacionadas às tecnologias, padrões, ou metodologias 
que serão usadas no seu trabalho, relacione-as de acordo com a ABNT.

Verifique no link abaixo como devem ser as referências no padrão ABNT:

http://www.pucminas.br/imagedb/documento/DOC\_DSC\_NOME\_ARQUI20160217102425.pdf

Por exemplo:

**[1]** - _ELMASRI, Ramez; NAVATHE, Sham. **Sistemas de banco de dados**. 7. ed. São Paulo: Pearson, c2019. E-book. ISBN 9788543025001._

**[2]** - _COPPIN, Ben. **Inteligência artificial**. Rio de Janeiro, RJ: LTC, c2010. E-book. ISBN 978-85-216-2936-8._

**[3]** - _CORMEN, Thomas H. et al. **Algoritmos: teoria e prática**. Rio de Janeiro, RJ: Elsevier, Campus, c2012. xvi, 926 p. ISBN 9788535236996._

**[4]** - _SUTHERLAND, Jeffrey Victor. **Scrum: a arte de fazer o dobro do trabalho na metade do tempo**. 2. ed. rev. São Paulo, SP: Leya, 2016. 236, [4] p. ISBN 9788544104514._

**[5]** - _RUSSELL, Stuart J.; NORVIG, Peter. **Inteligência artificial**. Rio de Janeiro: Elsevier, c2013. xxi, 988 p. ISBN 9788535237016._



# APÊNDICES

**Colocar link:**

Do código (armazenado no repositório);

Dos artefatos (armazenado do repositório);

Da apresentação final (armazenado no repositório);

Do vídeo de apresentação (armazenado no repositório).




