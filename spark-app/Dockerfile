# Nous utilisons une image qui contient déjà Spark et Python
FROM bitnami/spark:3.3.0

# Copiez notre script de processeur Spark dans le conteneur
COPY spark_processor.py /app/spark_processor.py
CMD ["/opt/bitnami/spark/bin/spark-submit", \
     "--master", "spark://spark-master:7077", \
     "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0,org.apache.spark:spark-avro_2.12:3.3.0", \
     "/app/spark_processor.py"]