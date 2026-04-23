# SmartFactory Lite

A real-time IIoT monitoring prototype simulating factory sensor data through an event-driven Kafka pipeline with live WebSocket push to clients.

Built as a self-directed project to explore production-style backend architecture: decoupled producers and consumers, streaming data, anomaly detection, and real-time delivery to browser clients.

## What it does

- Simulates industrial sensors producing temperature and vibration data every second
- Streams sensor data through Apache Kafka for decoupled, scalable delivery
- Flask-SocketIO consumer processes the Kafka stream, runs real-time anomaly detection, and pushes results to connected clients via WebSocket
- Kafka infrastructure runs locally via Docker Compose

## Architecture

```
Sensor Simulator  →  Kafka Broker  →  Flask-SocketIO Consumer  →  WebSocket Clients
                                      (anomaly detection)
```

## Tech Stack

| Layer         | Tech                         |
|---------------|------------------------------|
| Messaging     | Apache Kafka (via Zookeeper) |
| Backend       | Flask, Flask-SocketIO        |
| Real-time     | WebSocket                    |
| Orchestration | Docker Compose               |

## Key design decisions

- **Kafka over direct HTTP calls**: decouples sensor producers from the backend. Sensors keep producing even if the consumer is temporarily offline, and Kafka's persistent buffer prevents data loss on consumer failure. Also enables multiple consumers (monitoring, storage, alerting) to process the same stream independently.

- **Flask-SocketIO for real-time push**: the sensor stream produces continuous updates that need to reach clients with minimal latency. WebSocket pushes updates at the sensor frequency without client-side polling overhead.

- **Anomaly detection at consumer layer**: keeps producers lightweight and moves processing logic to a scalable layer. Current rules are simple thresholds (temperature > 70 or vibration > 0.1), but the pattern supports extending to ML-based detection later.

- **Separate simulator process**: mirrors real-world architecture where sensors operate independently from the processing layer. Makes it straightforward to swap the simulator for real sensor input later without changing the consumer.

- **Docker Compose for Kafka infrastructure**: running Kafka locally requires both the broker and Zookeeper. Compose defines them in a single file and starts the full Kafka setup with one command, making the environment reproducible for anyone who clones the repo.

## Running locally

```bash
# Start Kafka infrastructure
cd kafka-docker
docker-compose up -d

# Install Python dependencies
cd ../backend
pip install -r requirements.txt

# Run the simulator (in one terminal)
cd ../simulator
python simulate.py

# Run the consumer + WebSocket server (in another terminal)
cd ../backend
python app.py

# Open websocket-test.html in a browser to see live data
```

## Author

Wan-Lin Yang — [GitHub](https://github.com/wanlinyang1111)
