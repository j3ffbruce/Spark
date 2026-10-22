# ⚡ PyDeequ Pipeline - Technical Documentation

Repositório dedicado à modularização de pipelines PySpark e validação de qualidade de dados estruturados com **PyDeequ**.

## 🚀 Introdução ao PyDeequ

O **PyDeequ** é uma biblioteca Python integrada ao ecossistema PySpark, desenvolvida para validar a qualidade de dados em larga escala diretamente sobre o motor do Apache Spark. Ela permite a execução distribuída de métricas, perfilamento e regras de validação sem a necessidade de extrair os dados do cluster.

## 🛠️ Principais Componentes e Estrutura do Código (`Spark/jobs/pydeequ`)

### 📊 Analyzer

Responsável pelo cálculo de métricas estatísticas e estruturais sobre o conjunto de dados. É segmentado em análises tabulares, colunares e colunares comparativas.

* `- AnalysisRunner`: Construtor responsável por estruturar e disparar as métricas computacionais, como contagem total de registros ou valores distintos em colunas específicas.
* `- AnalysisContext`: Objeto de retorno que captura as métricas calculadas pelo runner e as expõe estruturadas em formato de DataFrame do Spark.

### 🔍 Profile

Responsável pelo mapeamento estrutural e estatístico dos dados.

* `- Column Profile Runner`: Efetua o perfilamento colunar automático para auxiliar no entendimento rápido da composição, distribuição de tipos e cardinalidade dos dados.

### 🛡️ Checks & VerificationResult

Representa o plano lógico de regras de negócio e a execução da auditoria de dados.

* `- Check`: Atua como a "prancheta" de regras de validação. Permite definir o nível de severidade (`CheckLevel.Error` ou `Warning`) e restrições customizadas sobre os dados (como limites de tamanho, verificação de nulos, unicidade e regras dinâmicas injetadas via funções `lambda`).
* `- VerificationSuite`: O motor inspetor que processa o conjunto de regras definidas no `Check` contra o DataFrame do Spark.
* `- VerificationResult`: Objeto resultante da execução da suíte de verificação, contendo o status detalhado de aprovação ou falha de cada restrição estipulada no `Check`.

### 💡 Suggestion

Módulo inteligente voltado para a descoberta automática de regras de qualidade com base na amostragem e nas características estruturais do dataset.

* `- ConstraintSuggestionRunner`: Construtor responsável por analisar o DataFrame e sugerir um conjunto inicial de restrições de qualidade com base no comportamento dos dados observados.

## 🔗 Links Úteis

| Descrição                                      | Nome do arquivo                                      |
| ---------------------------------------------- | ---------------------------------------------------- |
| Documentação oficial do PyDeequ (inglês)       | [pydeequ-doc-en.pdf](doc/pydeequ-doc-en.pdf)         |