#!/usr/bin/env python3
"""Send deployment notifications to Slack."""
import json, os, urllib.request

def send_notification(message, webhook_url=None):
    url = webhook_url or os.environ.get("SLACK_WEBHOOK")
    if not url:
        print("Warning: no Slack webhook configured")
        return
    data = json.dumps({"text": message}).encode()
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    urllib.request.urlopen(req)

if __name__ == "__main__":
    import sys
    send_notification(sys.argv[1] if len(sys.argv) > 1 else "Deployment complete.")
