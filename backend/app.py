from flask import Flask
from flask_socketio import SocketIO
from kafka import KafkaConsumer
import json

# TODO: Threading mode doesn't broadcast sensor_data events to frontend correctly.
# Backend Kafka pipeline works; WebSocket handshake succeeds but events don't reach client.
# Needs investigation into Flask-SocketIO threading mode + background task interaction.

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

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

        abnormal = False
        if data['temperature'] > 70 or data['vibration'] > 0.1:
            abnormal = True
            print("⚠️ 異常偵測！溫度或震動超標！")

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
