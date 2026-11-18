# DevOps Monitoring Platform

A containerized monitoring platform for tracking backend application health, HTTP traffic, response times, CPU usage, and memory usage.

## Project Overview

The DevOps Monitoring Platform uses Docker, FastAPI, Prometheus, and Grafana to monitor a backend application.

## Technology Stack

- **Backend:** Python 3.13, FastAPI
- **Containerization:** Docker and Docker Compose
- **Metrics Collection:** Prometheus
- **Monitoring Dashboard:** Grafana
- **CI/CD:** GitHub Actions
- **Container Registry:** Docker Hub

## Architecture

The platform consists of three main services:

1. **Backend:** Provides the API and exposes application metrics.
2. **Prometheus:** Collects metrics from the backend.
3. **Grafana:** Displays monitoring data through dashboards.

## Services and URLs

| Service | Local URL |
|---|---|
| Backend API | http://localhost:8000 |
| Backend Health | http://localhost:8000/health |
| Backend Metrics | http://localhost:8000/metrics |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:4000 |

## Monitoring Features

The Grafana dashboard includes:

- Backend health status
- HTTP error rate
- HTTP response time
- Total HTTP requests
- HTTP request rate
- Backend CPU usage
- Backend memory usage
- HTTP response time (P95)
- HTTP traffic by endpoint
- HTTP requests by status code

## Docker Deployment

### Prerequisites

- Docker Desktop
- Docker Compose
- Git

### Start the Platform

Clone the repository:

```bash
git clone https://github.com/IMjaveediqbal/devops-monitoring-platform.git
```

Navigate to the project directory:

```bash
cd devops-monitoring-platform
```

Pull the latest backend image:

```bash
docker compose pull
```

Start all services:

```bash
docker compose up -d
```

### Check Running Containers

```bash
docker compose ps
```

### Stop the Platform

```bash
docker compose down
```

## Docker Hub Image

The backend image is published on Docker Hub:

`javeediqbal/devops-backend:latest`

## Health Check

To verify that the backend is working:

```bash
curl http://localhost:8000/health
```

Expected response:

```json
{
  "status": "ok"
}
```

## Prometheus Metrics

The backend exposes metrics at:

`http://localhost:8000/metrics`

Prometheus collects these metrics using the configured scrape target:

`backend:8000`

## CI/CD Pipeline

GitHub Actions automates the backend Docker image build and publishing process.

The workflow builds and publishes:

- `javeediqbal/devops-backend:latest`
- A commit-specific image tag

## Repository

GitHub: https://github.com/IMjaveediqbal/devops-monitoring-platform

## Project Status

The Docker-based deployment has been tested. The backend, Prometheus, and Grafana services have been started and verified.

---

**DevOps Monitoring Platform**

*Built with Docker, FastAPI, Prometheus, and Grafana.*