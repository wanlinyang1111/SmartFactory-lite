from kafka import KafkaProducer
import json
import random
import time

# Initialize Kafka Producer connecting to local Kafka broker
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize Python dict to JSON bytes
)

def generate_sensor_data():
    # Generate simulated sensor data with random temperature and vibration values
    return {
        "temperature": round(random.uniform(20, 90), 2),  # Random temperature between 20 and 90 degrees
        "vibration": round(random.uniform(0.01, 0.2), 3)  # Random vibration between 0.01 and 0.2
    }

while True:
    data = generate_sensor_data()  # Generate data
    print("Sending:", data)  # Log data to console
    producer.send("sensor-data", value=data)  # Send data to Kafka topic 'sensor-data'
    time.sleep(1)  # Wait 1 second before sending next message
