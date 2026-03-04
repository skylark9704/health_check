# Health Check Service

A simple health check service written in Python and containerized with Docker.

## Running the service

```bash
docker compose up -d
```

The service will be available on the host machine at `http://localhost:4444/`.

### Endpoints
- `/` or `/health`: Returns `OK`
