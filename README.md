# Simple AWS Data Lake

Projeto de Engenharia de Dados que implementa um Data Lake simples na AWS
utilizando Amazon S3, PySpark, Apache Parquet e Amazon Athena.

## Arquitetura

```text
CSV
 ↓
Amazon S3 - Bronze
 ↓
PySpark
 ↓
Limpeza e transformação
 ↓
Apache Parquet
 ↓
Amazon S3 - Silver
 ↓
Amazon Athena
 ↓
Consultas SQL
cd /mnt/c/Users/leona/simple-aws-data-lake

# Padroniza a branch como main
git branch -m main

# Cria requirements.txt
cat > requirements.txt <<'EOF'
pyspark==4.2.0
