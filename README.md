# Phoenix Deploy

Internal deployment tooling for Project Phoenix.

## Quick Start

```bash
pip install -r requirements.txt
cp config/dev.env.example config/dev.env
python deploy.py --env staging --target all
```

## Local Development

```bash
docker-compose up -d
python healthcheck.py http://localhost:8080
```

## Rollback

```bash
python rollback.py api --env production
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).
