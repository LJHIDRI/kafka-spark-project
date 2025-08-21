import time
import json
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import random

# Producer configuration
producer = None
while producer is None:
    try:
        # Nous utilisons maintenant KafkaProducer de kafka-python
        producer = KafkaProducer(
            bootstrap_servers='kafka:9092',
            # Le sérialiseur convertit notre dictionnaire Python en une chaîne JSON, puis en bytes
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        print("JSON Producer connected to Kafka successfully.")
    except NoBrokersAvailable:
        print("Waiting for Kafka broker to be available...")
        time.sleep(5)


# Sample data - La structure reste la même
users = ["user1@example.com", "user2@example.com", "user3@example.com"]
urls = ["/home", "/products/1", "/checkout", "/contact"]
topic = 'user-clicks' # Nous gardons le même topic

print(f"Producing JSON records to topic '{topic}'. Press Ctrl-C to exit.")
while True:
    try:
        # Créer le message
        value = {
            "email": random.choice(users),
            "url": random.choice(urls),
            "timestamp": int(time.time() * 1000) # Spark aime les timestamps longs
        }

        producer.send(topic, value=value)
        print(f"Sent JSON record: {value}")
        
        producer.flush()
        time.sleep(random.uniform(0.5, 3.0))

    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"An error occurred: {e}")