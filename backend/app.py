import eventlet
eventlet.monkey_patch()
from flask import Flask
from flask_socketio import SocketIO
from kafka import KafkaConsumer
import json
import threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins=["http://localhost:8080"], async_mode='eventlet')




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

        # ☑️ 這裡可以加入異常判斷邏輯
        if data['temperature'] > 70 or data['vibration'] > 0.1:
            print("⚠️  異常偵測！溫度或震動超標！")

        # 🔄 透過 WebSocket 推送到前端
        socketio.emit('sensor_data', data)

@app.route('/')
def index():
    return "SmartFactory Lite backend + WebSocket is running."

if __name__ == '__main__':
    # ✅ 正確：使用 socketio 的背景任務方式
    socketio.start_background_task(consume_kafka)

    # ✅ 用 eventlet 啟動 Flask + WebSocket server
    socketio.run(app, debug=True, port=5000)


