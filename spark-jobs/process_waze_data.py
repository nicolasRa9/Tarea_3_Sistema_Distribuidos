from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType
from pyspark.sql.functions import from_json, col

# Configuración del SparkSession
spark = SparkSession.builder \
    .appName("WazeDataProcessor") \
    .getOrCreate()

# Leer datos desde Kafka
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "waze-alerts") \
    .load()

# Definir el esquema de los datos
schema = StructType() \
    .add("title", StringType()) \
    .add("description", StringType()) \
    .add("severity", StringType()) \
    .add("coordinates", StringType())

# Parsear los datos
parsed_df = kafka_df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Mostrar datos en consola (solo para depuración)
query = parsed_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
