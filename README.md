# 📄 README.md — SmartFactory Lite

SmartFactory Lite is a real-time industrial monitoring platform that simulates and tracks sensor data (like temperature and vibration) to demonstrate a scalable, event-driven system architecture. The system is designed as a multi-module, modern backend infrastructure project suitable for showcasing skills in distributed systems, cloud infrastructure, real-time data handling, and DevOps workflows.

This repository presents a working prototype of how factories can monitor real-time sensor feeds, detect anomalies, and prepare for downstream integrations like alerts, dashboards, and databases. While the project is under active development, the architectural foundation already reflects core principles used in production-level systems.

---

## 💡 Project Vision

- Create an extensible backend system simulating industrial IoT data pipelines
- Apply Kafka-based streaming for real-time, decoupled data flow
- Enable integration with multiple modules: monitoring, visualization, alerting, and persistence
- Support scalable, production-style deployment using Docker Compose

---

## 🔧 Core Modules

- **Sensor Simulator**: Mocks data every second to simulate real factory conditions.
- **Kafka Pipeline**: Acts as the core data stream buffer, decoupling producers and consumers.
- **Flask Backend**: Listens to Kafka stream and processes incoming sensor data.
- **WebSocket Server** *(upcoming)*: Pushes data in real-time to frontend dashboards.
- **React Dashboard** *(upcoming)*: Visualizes live sensor metrics with real-time charts.
- **Future Add-ons**: Alerting (Slack/LINE), Persistence (PostgreSQL), Observability (Grafana), CI/CD automation.

---

## 🚧 Development Status

This project is in-progress and being actively built out over several weeks. Functional milestones include:

- ✅ Simulated data production via Kafka
- ✅ Real-time Kafka consumer backend with anomaly detection
- 🔄 WebSocket + frontend live integration (in progress)
- 🧱 Storage, monitoring, and deployment features (planned)

---

## 👀 Who Is This For?

This project is ideal for:
- Students or engineers building portfolio projects for systems/backend/infrastructure roles
- Developers exploring Kafka and real-time data processing
- Teams needing a lightweight prototype for IIoT monitoring pipelines

---

This README is a living document and will be fully updated when the project reaches a publish-ready milestone.
