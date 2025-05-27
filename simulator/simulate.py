from kafka import KafkaProducer
import json
import random
import time

# 初始化 Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_sensor_data():
    return {
        "temperature": round(random.uniform(20, 90), 2),
        "vibration": round(random.uniform(0.01, 0.2), 3)
    }

while True:
    data = generate_sensor_data()
    print("Sending:", data)
    # 送到 Kafka topic 名稱為 sensor-data
    producer.send("sensor-data", value=data)
    time.sleep(1)
