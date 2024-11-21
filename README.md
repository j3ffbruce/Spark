# PySpark Scripts Templates

Bem-vindo ao repositório de **Scripts Templates do PySpark**! Este repositório contém modelos de scripts PySpark, exemplos de uso e uma infraestrutura Docker para executar esses scripts em um ambiente distribuído do Spark.

## 🚀 Introdução

O **Apache Spark** é um mecanismo de processamento paralelo de código aberto, projetado para processar grandes volumes de dados de maneira distribuída. Este repositório fornece scripts de exemplo que podem ser facilmente adaptados para diversos cenários de processamento de dados com PySpark.

## 📋 Pré-requisitos

Antes de começar, certifique-se de que você possui as seguintes dependências instaladas:

- **Docker**: Uma plataforma para automatizar a execução de aplicativos dentro de containers. Instale o Docker a partir do site oficial: [Docker Install](https://docs.docker.com/get-docker/).
- **Docker Compose**: Uma ferramenta para definir e executar aplicativos Docker multi-contêiner. Siga as instruções de instalação em [Docker Compose Install](https://docs.docker.com/compose/install/).

## 📁 Estrutura do Repositório

A estrutura do repositório é organizada da seguinte maneira:

- **`README.md`**: Este arquivo, que fornece uma visão geral do repositório e instruções de uso.
- **`docker-compose.yml`**: Arquivo de configuração para provisionar a infraestrutura do Spark usando Docker Compose.
- **`apps/`**: Pasta contendo todos os jobs de exemplo em PySpark.

## ⚙️ Ambiente  (Docker)

### 📋 Pré-requisitos

Antes de começar, certifique-se de que você possui as seguintes dependências instaladas:

- **Docker**: Uma plataforma para automatizar a execução de aplicativos dentro de containers. Instale o Docker a partir do site oficial: [Docker Install](https://docs.docker.com/get-docker/).
- **Docker Compose**: Uma ferramenta para definir e executar aplicativos Docker multi-contêiner. Siga as instruções de instalação em [Docker Compose Install](https://docs.docker.com/compose/install/).

## 🛠️ Como Usar

Para utilizar este repositório, siga os passos abaixo:

1. **Clone o repositório**:

   Execute o seguinte comando para clonar o repositório em sua máquina local:

   ```bash
   git clone https://github.com/j3ffbruce/Spark.git
   ```
2. **Navegue até o repositório**:

   Após clonar, navegue para a pasta do repositório:

   ```bash
   cd Spark
   ```

3. **Suba a infraestrutura usando Docker Compose**:

   Com o Docker Compose, você pode levantar os containers necessários para o ambiente Spark. Execute o seguinte comando:

   ```bash
   docker-compose up -d
   ```

4. **Executar scripts PySpark:**

    Após a infraestrutura estar configurada, você pode executar seus scripts PySpark dentro do ambiente Docker com os seguintes comandos:

    Acessar o ambiente de processamento:

    ```bash
    docker exec -it spark-client bash
    ```

    Executar o Script de Processamento no Ambiente Spark

    ```bash
    /opt/spark/bin/spark-submit --master spark://spark-master:7077 --conf spark.ui.showConsoleProgress=false --conf spark.log.level=WARN /opt/spark-apps/test_spark.py 
    ```

## 📧 Contato

Para perguntas ou sugestões, entre em contato comigo no [GitHub](https://github.com/j3ffbruce) ou no [LinkedIn](https://www.linkedin.com/in/jefferson-alves-15732513b/).