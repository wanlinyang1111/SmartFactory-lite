from flask import Flask
from kafka import KafkaConsumer
import json
import threading

app = Flask(__name__)

# 🧵 Kafka 消費者背景執行
def consume_kafka():
    consumer = KafkaConsumer(
        'sensor-data',
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='latest',
        enable_auto_commit=True,
        group_id='smartfactory-group'
    )
    print("🟢 Kafka Consumer started. Listening to 'sensor-data'...")
    for message in consumer:
        data = message.value
        print(f"📥 Received from Kafka: {data}")

        # ☑️ 這裡你可以加入異常判斷邏輯
        if data['temperature'] > 70 or data['vibration'] > 0.1:
            print("⚠️  異常偵測！溫度或震動超標！")

@app.route('/')
def index():
    return "SmartFactory Lite backend is running."

if __name__ == '__main__':
    # 🎯 啟動 Kafka Consumer 背景執行緒
    t = threading.Thread(target=consume_kafka)
    t.daemon = True
    t.start()

    # 🚀 啟動 Flask Server
    app.run(debug=True, port=5000)
