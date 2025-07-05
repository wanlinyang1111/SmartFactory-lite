import eventlet
eventlet.monkey_patch()

from flask import Flask
from flask_socketio import SocketIO
from kafka import KafkaConsumer
import json

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins=["http://localhost:8080"], async_mode='eventlet')

@app.route('/')
def index():
    return "OK"

def consume_kafka():
    consumer = KafkaConsumer(
        'sensor-data',
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='latest',
        group_id='smartfactory-group'
    )
    for message in consumer:
        data = message.value
        print("Received from Kafka:", data)

        # 判斷異常
        abnormal = False
        if data['temperature'] > 70 or data['vibration'] > 0.1:
            abnormal = True
            print("⚠️ 異常偵測！溫度或震動超標！")

        # 連同是否異常的標記一起送給前端
        data['abnormal'] = abnormal
        socketio.emit('sensor_data', data)


@socketio.on('connect')
def on_connect():
    print('Client connected')

@socketio.on('disconnect')
def on_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.start_background_task(consume_kafka)
    socketio.run(app, host="0.0.0.0", port=5050, debug=True)
