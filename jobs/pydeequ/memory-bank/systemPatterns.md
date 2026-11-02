# systemPatterns - jobs/pydeequ

Pipeline linear, classes por etapa, sem orquestrador externo.

```
Extract -> Transform -> Quality -> spark.stop()
```

| Modulo | Papel |
|---|---|
| `Extract` | CSV `datasets/csv/movies`: `header=True`, `sep=";"`, `encoding="UTF-16"`, `inferSchema=True` |
| `Transform` | Rename da coluna CNPJ com char extra no schema -> `CNPJ_DISTRIBUIDORA`; trim 1 char no CNPJ |
| `Quality` | Size, Completeness/CountDistinct/Compliance; profile `TITULO_BRASIL`,`PUBLICO`; Check Warning unique+non-negative `PUBLICO`; ConstraintSuggestion em `PUBLICO` |

Saidas de analyzer/profile/check estao comentadas; so suggestions imprimem no `run()`.

Convencao: etapa expoe `run()`. Spark so em Extract/Quality; Transform opera no DataFrame.