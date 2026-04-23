# SmartFactory Lite

A real-time IIoT monitoring prototype simulating factory sensor data through an event-driven Kafka pipeline.

Built as a self-directed project to explore production-style backend architecture: decoupled producers and consumers, streaming data, and anomaly detection at the processing layer.

## What it does

- Simulates industrial sensors (temperature, vibration) producing data every second
- Streams sensor data through Apache Kafka for decoupled, scalable message delivery
- Flask consumer processes the Kafka stream and runs real-time anomaly detection
- Runs locally via Docker Compose for reproducible multi-service development

## Architecture

```
Sensor Simulator  →  Kafka Broker  →  Flask Consumer (with anomaly detection)
```

## Tech Stack

| Layer         | Tech                  |
|---------------|-----------------------|
| Messaging     | Apache Kafka          |
| Backend       | Flask, Python         |
| Orchestration | Docker Compose        |

## Key design decisions

- **Kafka over direct HTTP calls**: decouples sensor producers from backend consumers. Sensors keep producing even if the consumer is temporarily offline, and Kafka's persistent buffer prevents data loss on consumer failure. Also enables multiple consumers (monitoring, storage, alerting) to process the same stream independently.

- **Separate simulator process**: mirrors real-world architecture where sensors operate independently from the processing layer. Makes it straightforward to swap the simulator for real sensor input later without changing the consumer.

- **Anomaly detection at consumer layer**: keeps producers lightweight and moves processing logic to a horizontally scalable layer that can be replicated as data volume grows.

- **Flask for the consumer**: the engineering focus of this project is the streaming architecture, not the HTTP layer. Flask is lightweight and sufficient for this scope. If the workload required high concurrency or async processing, FastAPI would be a natural upgrade path.

- **Docker Compose for orchestration**: running Kafka broker, simulator, and consumer as three separate services locally is painful without orchestration. Compose defines the full dev environment in one file, making the project reproducible for anyone who clones the repo.

## Running locally

```bash
# Start Kafka
cd kafka-docker
docker-compose up -d

# Run the simulator
cd ../simulator
python simulator.py

# Run the consumer
cd ../backend
python consumer.py
```

## Author

Wan-Lin Yang — [GitHub](https://github.com/wanlinyang1111)
