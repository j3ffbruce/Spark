# Instruções para Criar e Ativar uma Virtual Environment (venv)

### 🛠️ **Criando uma venv**

1. **Instalar o Python (caso ainda não tenha instalado)**:
   
   Se você ainda não tem o Python instalado, faça o download e instale a versão mais recente do Python no [site oficial](https://www.python.org/downloads/).

2. **Criando o ambiente virtual (venv)**:
   
   Abra o terminal ou prompt de comando no diretório onde deseja criar o ambiente virtual e execute o comando abaixo:

   - No **Windows**:
     ```bash
     python -m venv .venv
     ```

   - No **Linux/MacOS**:
     ```bash
     python3 -m venv .venv
     ```

   O comando irá criar uma pasta chamada `.venv` no seu projeto que conterá todos os pacotes necessários para o ambiente isolado.

---

### 🟢 **Ativando a venv**

Depois de criar a venv, você precisará ativá-la antes de instalar qualquer dependência. Abaixo estão os comandos para ativar a venv de acordo com o seu sistema operacional:

- No **Windows**:
  ```bash
  .\.venv\Scripts\activate

### ❌ **Desativando a Virtual Environment (venv)**

Após terminar o trabalho no ambiente virtual, você pode desativá-lo facilmente com o seguinte comando:

- **No Windows, Linux e MacOS**:
  ```bash
  deactivate

### 📦 **Instalando Dependências com o `requirements.txt`**

   Use o comando `pip` para instalar todas as dependências listadas no arquivo `requirements.txt`:

- **CLI - Command**:
  ```bash
  pip install -r requirements.txt

### 🚀 **Rodando o Projeto Localmente com o Spark**
   Use o comando `pip` para instalar todas as dependências listadas no arquivo `requirements.txt`:

- **CLI - Command**:
  ```bash
   spark-submit --conf "spark.pyspark.python=./.venv/Scripts/python.exe" --conf "spark.pyspark.driver.python=./.venv/Scripts/python.exe" main.py
