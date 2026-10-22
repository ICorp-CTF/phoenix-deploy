#!/usr/bin/env python3
"""Quick rollback to the previous deployment version."""
import subprocess
import sys

def rollback(service):
    tag = f"{service}-prev"
    print(f"Rolling back {service} to tag: {tag}")
    subprocess.run(["docker", "pull", f"registry.icorp.internal/{service}:{tag}"], check=True)
    subprocess.run(["docker", "service", "update", "--image",
                     f"registry.icorp.internal/{service}:{tag}", service], check=True)
    print(f"Rollback complete for {service}.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: rollback.py <service-name>")
        sys.exit(1)
    rollback(sys.argv[1])
