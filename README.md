# ⚡ Spark

Ambiente de estudos para **Apache Spark / PySpark**.

## 🛠️ Technical Stack

| Componente | Versão     |
| ---------- | ---------- |
| 💻 OS      | Windows    |
| 🐍 Python  | 3.10+      |
| ☕ Java     | 17         |
| ⚡ PySpark  | 3.5.6      |
| 🖥️ Shell  | PowerShell |

## 📋 Pré-requisitos

☕ **Java 17 instalado** através do link: https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html

```text
environment/dependencies/java/
```

> ⚠️ O Java deve estar instalado antes da execução do script `env.ps1`.

## 📁 Repository Structure

```text
.
├── environment/
│   └── scripts/
│       └── env.ps1
│
├── jobs/
│
└── requirements.txt
```

## 📦 Dependencies

`requirements.txt`:

```text
pyspark==3.5.6
```

## ⚙️ Environment Configuration

O script `environment/scripts/env.ps1` configura as variáveis de ambiente necessárias para execução do PySpark.

▶️ Executar:

```powershell
.\environment\scripts\env.ps1
```

## 🐍 Python Environment

### Criar o virtual environment

```powershell
python -m venv .venv
```

### ▶️ Ativar

```powershell
.\.venv\Scripts\Activate.ps1
```

### 📦 Instalar as dependências

```powershell
pip install -r requirements.txt
```

## ✅ Validação

```powershell
java -version
python --version
python -c "import pyspark; print(pyspark.__version__)"
```

Versões esperadas:

```text
Java:    17
PySpark: 3.5.6
```

## 🚀 Execution

Os jobs PySpark estão armazenados em:

```text
jobs/
```

▶️ Execução:

```powershell
./enviroment/scripts/env.ps1; python ./jobs/dummy_job/main.py
```
