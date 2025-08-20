from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, LongType

# 1. Créer une SparkSession
# La configuration des packages est maintenant dans le Dockerfile, donc plus besoin ici
spark = SparkSession.builder \
    .appName("ClickstreamProcessorJSON") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

print("Session Spark créée. Lecture du stream Kafka en format JSON...")

# 2. Lire le stream depuis Kafka (cette partie ne change pas)
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "user-clicks") \
    .option("startingOffsets", "earliest") \
    .load()

# 3. Convertir la colonne 'value' (qui est en binaire) en une chaîne de caractères
df_string = kafka_df.selectExpr("CAST(value AS STRING) as json_value")

# 4. Définir le schéma qui correspond EXACTEMENT à notre JSON
# C'est l'équivalent de notre schéma Avro, mais pour JSON
schema = StructType() \
    .add("email", StringType()) \
    .add("url", StringType()) \
    .add("timestamp", LongType())

# 5. Parser la chaîne JSON en utilisant le schéma
df_parsed = df_string.select(from_json(col("json_value"), schema).alias("data")).select("data.*")

print("Schema du DataFrame après parsing JSON :")
df_parsed.printSchema()

# 6. L'analyse reste la même : compter les clics par URL
url_counts = df_parsed.groupBy("url").count()

# 7. Afficher le résultat dans la console (cette partie ne change pas)
query = url_counts.writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", "false") \
    .start()

print("Le streaming a commencé. En attente de données...")
query.awaitTermination()