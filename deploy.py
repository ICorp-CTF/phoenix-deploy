#!/usr/bin/env python3
"""iCorp deployment tool for Project Phoenix."""

import argparse
import os
import sys


def load_config(env):
    config_path = f"config/{env}_credentials.env"
    if not os.path.exists(config_path):
        print(f"Error: config file not found: {config_path}")
        print("  Hint: copy config/settings.yaml.example and fill in values.")
        sys.exit(1)
    config = {}
    with open(config_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, _, value = line.partition("=")
                config[key.strip()] = value.strip()
    return config


def deploy(env, target):
    try:
        config = load_config(env)
    except Exception as e:
        print(f"Error loading config for {env}: {e}", file=sys.stderr)
        sys.exit(1)

    required = ["DB_HOST", "API_URL"]
    missing = [k for k in required if k not in config]
    if missing:
        print(f"Error: missing config keys: {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)

    print(f"Deploying to {target} ({env})...")
    print(f"  Database: {config['DB_HOST']}")
    print(f"  API endpoint: {config['API_URL']}")
    print("  Deployment complete.")


def main():
    parser = argparse.ArgumentParser(description="Deploy Project Phoenix")
    parser.add_argument("--env", required=True, choices=["staging", "production"])
    parser.add_argument("--target", required=True)
    args = parser.parse_args()
    deploy(args.env, args.target)


if __name__ == "__main__":
    main()
