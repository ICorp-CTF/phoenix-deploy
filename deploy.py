#!/usr/bin/env python3
"""iCorp deployment tool for Project Phoenix."""

import argparse
import os
import sys


def load_config(env):
    config_path = f"config/{env}_credentials.env"
    if not os.path.exists(config_path):
        print(f"Error: config file not found: {config_path}")
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
    config = load_config(env)
    print(f"Deploying to {target} ({env})...")
    print(f"  Database: {config.get('DB_HOST', 'unknown')}")
    print(f"  API endpoint: {config.get('API_URL', 'unknown')}")
    print("  Deployment complete.")


def main():
    parser = argparse.ArgumentParser(description="Deploy Project Phoenix")
    parser.add_argument("--env", required=True, choices=["staging", "production"])
    parser.add_argument("--target", required=True)
    args = parser.parse_args()
    deploy(args.env, args.target)


if __name__ == "__main__":
    main()
