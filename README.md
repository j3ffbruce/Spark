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
- **`Dockerfile`**: Arquivo de configuração com as especificações para o ambiente Docker.
- **`docker-compose.yml`**: Arquivo de configuração para provisionar a infraestrutura do Spark usando Docker Compose.
- **`jobs/`**: Pasta contendo todos os jobs de exemplo em PySpark.
  - **`project_/`**: Todos jobs estarão alocados em pastas prefixadas com project_

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

3. **Construa a imagem Docker**:

   Utilize o comando abaixo para construir a imagem Docker a partir do Dockerfile:

   ```bash
   docker build -t spark-environment .
   ```
4. **Suba a infraestrutura usando Docker Compose**:

   Com o Docker Compose, você pode levantar os containers necessários para o ambiente Spark. Execute o seguinte comando:

   ```bash
   docker-compose up -d
   ```

5. **Executar scripts PySpark:**:

    Após a infraestrutura estar configurada, você pode executar seus scripts PySpark dentro do ambiente Docker com os seguintes comandos:

    Para rodar um script Pyspark meu_script.py

    ```bash
    docker exec -it spark-master spark-submit --master spark://spark-master:7077 /jobs/project_folder/main.py
    ```

    Para rodar um script Pytest meu_test.py

    ```bash
    docker exec -it spark-master pytest -v --disable-warnings /scripts/project_01/test_script.py
    ```
### ❗ Observações:

- As dependências externas devem ser mapeadas no arquivo `Dockerfile`, caso necessário.
- Para configurar e utilizar um ambiente local, siga este tutorial:  
  [Guia passo a passo para instalar PySpark no Windows](https://medium.com/@deepaksrawat1906/a-step-by-step-guide-to-installing-pyspark-on-windows-3589f0139a30).
- Para rodar scripts usando uma `venv` em um ambiente local, utilize o seguinte comando:

  ```bash
  spark-submit \
    --conf "spark.pyspark.python=.venv/Scripts/python.exe" \
    --conf "spark.pyspark.driver.python=.venv/Scripts/python.exe" \
    main.py


## 📧 Contato

Para perguntas ou sugestões, entre em contato comigo no [GitHub](https://github.com/j3ffbruce) ou no [LinkedIn](https://www.linkedin.com/in/jefferson-alves-15732513b/).