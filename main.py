import os
import json
import requests

SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')
CHANNEL_ID = os.getenv('INPUT_CHANNEL_ID')  # 채널 ID를 입력으로 받음

def send_message(message):
    payload = {
        "channel": CHANNEL_ID,
        "text": message
    }
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    if response.status_code != 200:
        raise Exception(f"Request to Slack returned an error {response.status_code}, {response.text}")

if __name__ == "__main__":
    messages = json.loads(os.getenv('INPUT_MESSAGES', '[]'))
    for message in messages:
        send_message(message)