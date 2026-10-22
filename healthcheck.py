#!/usr/bin/env python3
"""Post-deployment health check for Phoenix services."""
import requests
import sys

ENDPOINTS = [
    "/api/v1/health",
    "/api/v1/status",
]

def check(base_url):
    for ep in ENDPOINTS:
        try:
            r = requests.get(f"{base_url}{ep}", timeout=5)
            if r.status_code != 200:
                print(f"FAIL: {ep} returned {r.status_code}")
                return False
        except requests.ConnectionError:
            print(f"FAIL: {ep} unreachable")
            return False
    print("All health checks passed.")
    return True

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8080"
    sys.exit(0 if check(url) else 1)
