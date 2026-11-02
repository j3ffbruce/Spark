# techContext - jobs/pydeequ

Fonte de verdade para versoes e runtime. Atualizar este arquivo quando `requirements.txt` ou `env.ps1` mudarem.

## Python / libs

| Artefato | Versao | Origem |
|---|---|---|
| pyspark | 3.5.6 | `requirements.txt` |
| pydeequ | 1.7.0 | `requirements.txt` |
| Spark (runtime) | 3.5 | `SPARK_VERSION` em `env.ps1`; `SPARK_HOME` vazio (Spark do PySpark) |
| venv | `jobs/pydeequ/.venv` | `env.ps1` |

Deequ JVM entra via `pydeequ.deequ_maven_coord`; `f2j_maven_coord` vai em `spark.jars.excludes`.

## JVM / Hadoop (Windows)

| Artefato | Versao / path |
|---|---|
| JDK | Eclipse Adoptium 17.0.20.101-hotspot (`JAVA_HOME`) |
| Hadoop | 3.3.5 (`C:\hadoop-3.3.5`) |
| PySpark Python | `.venv\Scripts\python.exe` (`PYSPARK_PYTHON` / `PYSPARK_DRIVER_PYTHON`) |

Bootstrap: `.\env.ps1` na pasta do job.

## Spark session (`main.py`)

- master: `local[*]`
- appName: `pyDeequ`
- log: `WARN`
- extra JAR: `/jobs/pydeequ/packages/dqdl-1.0.0.jar` (`spark.jars`)

## Superficie PyDeequ usada

`analyzers`, `profiles`, `verification`, `checks`, `suggestions` - ver `modules/quality.py`.