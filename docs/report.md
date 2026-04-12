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

### Requisitos 

##### Requisitos Funcionais (RF)
- RF01: O sistema deve permitir o upload e processamento de datasets de reclamações em formato CSV/JSON.

- RF02: O sistema deve calcular o índice de "Morte Prematura" (relação entre tempo de compra e tempo de falha).

- RF03: O sistema deve gerar rankings de fabricantes por categoria de produto.

- RF04: O sistema deve oferecer filtros por região, marca e tipo de defeito.

#### Requisitos Não Funcionais (RNF)
- RNF01: O backend deve ser capaz de realizar agregações em bases de dados superiores a 10.000 registros com tempo de resposta inferior a 2 segundos.

- RNF02: Os dados processados devem ser persistidos em banco de dados relacional para garantir integridade.

- RNF03: A interface deve seguir padrões de acessibilidade para visualização de gráficos.

## Análise exploratórida dos dados

###    Dicionário de dados

Apresente uma descrição das bases de dados a serem utilizadas. 
Dicionários de dados devem conter as bases de dados, os nomes dos atributos 
com seu significado, seu tipo (inteiro, real, textual, categórico, etc).

Este projeto deve utilizar pelo menos duas fontes de dados. Uma fonte principal e 
uma fonte para enriquecimentos dos dados principais.


###    Descrição de dados

Utilize a análise descritiva baseada em estatística de primeira ordem para descrever os dados.
Como descrever dados numéricos: média, desvio padrão, mínimo, máximo, quartis, histograma, etc.
Como descrever dados qualitativos (categóricos): moda (valor mais frequente), quantidade de valores distintos (categorias), distribuição das categorias (histograma), etc.


## Preparação dos dados

A preparação dos dados consiste dos seguintes passos:

> - Seleção dos atributos
> - Tratamentos dos valores faltantes ou omissos: remoção, substituição, indução, etc.
> - Tratamento dos valores inconsistentes: conversão, remoção de dados duplicados, remoção ou tratamento de ouliers.
> - Conversão de dados: p. ex. numérico para categórico, categórico para binário, etc.


## Indução de modelos

### Modelo 1: Algoritmo

Substitua o título pelo nome do algoritmo que será utilizado. P. ex. árvore de decisão, rede neural, SVM, etc.
Justifique a escolha do modelo.
Apresente o processo utilizado para amostragem de dados (particionamento, cross-validation).
Descreva os parâmetros utilizados. 
Apresente trechos do código utilizado comentados. Se utilizou alguma ferramenta gráfica, apresente imagens
com o fluxo de processamento.

### Modelo 2: Algoritmo

Repita os passos anteriores para o segundo modelo.


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




