# Phoenix Deploy

Internal deployment tooling for Project Phoenix.

## Usage

```bash
python deploy.py --env production --target api
```

## Health Check

```bash
python healthcheck.py https://phoenix.icorp.internal
```

## Configuration

Copy `config/config.template.env` to `config/production.env` and fill in your values.
**Never commit credentials to this repository.**

## Team

- Erik Nilsson (maintainer)
- Sara Lindberg (deployment automation)
