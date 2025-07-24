# local-prometheus

A minimal local monitoring stack using Prometheus and Grafana, designed for quick setup and local development.

## Description

This project provides a ready-to-use local monitoring environment for developers. It uses Docker Compose to orchestrate Prometheus for metrics collection and Grafana for visualization. All configurations, datasources, and dashboards are pre-provisioned for a seamless experience.

## Features

- **Prometheus**: Collects and stores metrics.
- **Grafana**: Visualizes metrics with dashboards.
- **Docker Compose**: Simple orchestration for both services.
- **Pre-configured provisioning**: Datasources and dashboards are automatically set up.

## Usage

1. Start the stack:
   ```sh
   docker-compose up
   ```
2. Access Prometheus at [http://localhost:9090](http://localhost:9090)
3. Access Grafana at [http://localhost:3000](http://localhost:3000) (default login: `admin` / `admin`)

## File Structure

- `prometheus.yml`: Prometheus configuration.
- `grafana/provisioning/datasources/`: Grafana datasource provisioning.
- `grafana/provisioning/dashboards/`: Grafana dashboard provisioning.
- `docker-compose.yml`: Service orchestration.

## License

MIT