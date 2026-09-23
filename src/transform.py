from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

spark = (
    SparkSession.builder
    .appName("trips-transform")
    .master("local[*]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

print("\n=== 1. LENDO CAMADA BRONZE ===")

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("data/trips.csv")
)

df.show()

print("Registros recebidos:", df.count())

print("\n=== 2. APLICANDO LIMPEZA ===")

clean_df = (
    df
    .dropDuplicates(["trip_id"])
    .filter(col("distance_km") > 0)
    .filter(col("fare_amount") > 0)
    .withColumn("trip_date", to_date("trip_date"))
)

clean_df.show()

print("Registros válidos:", clean_df.count())

print("\n=== 3. SCHEMA DA CAMADA SILVER ===")

clean_df.printSchema()

print("\n=== 4. GRAVANDO PARQUET ===")

(
    clean_df.write
    .mode("overwrite")
    .parquet("output/silver/trips")
)

print("Parquet gravado com sucesso.")

print("\n=== 5. VALIDANDO O PARQUET ===")

silver_df = spark.read.parquet("output/silver/trips")

silver_df.show()
silver_df.printSchema()

print("Registros encontrados no Parquet:", silver_df.count())

spark.stop()

print("\nPIPELINE LOCAL CONCLUÍDO COM SUCESSO.")
