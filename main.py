import os
import json
import requests

# 환경 변수에서 값 읽기
SLACK_WEBHOOK_URL = os.getenv('slack-webhook-url')
ACTOR = os.getenv('actor', 'ghkdqhrbals')
MESSAGE_LIST = json.loads(os.getenv('messages', '[]'))
MESSAGE_TITLE = os.getenv('message-title', 'Slack Alert List')
COLOR = os.getenv('color', '#3bb143')

print("SLACK_WEBHOOK_URL2342134123412341234:", os.getenv('SLACK_WEBHOOK_URL'))
print("ACTOR123:", os.getenv('ACTOR'))
print("MESSAGES:", os.getenv('MESSAGES'))
print("MESSAGE_TITLE:", os.getenv('MESSAGE_TITLE'))
print("COLOR:", os.getenv('COLOR'))

ACTOR_PROFILE_URL = f'https://github.com/{ACTOR}' if ACTOR else 'https://github.com'

def build_slack_payload(actor, actor_profile_url, message_title, message_list, color):
    attachments = [
        {
            "color": color,
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "\n".join([f"• {item}" for item in message_list])
                    }
                }
            ]
        }
    ]
    return {
        "username": "Slack Bot",
        "icon_emoji": ":robot_face:",
        "text": f"{message_title} (by <{actor_profile_url}|{actor}>)",
        "attachments": attachments
    }

def send_slack_message(payload, slack_webhook_url):
    response = requests.post(slack_webhook_url, json=payload)
    if response.status_code == 200:
        print("Slack message sent successfully.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")
        exit(1)

# 메시지 전송
slack_payload = build_slack_payload(ACTOR, ACTOR_PROFILE_URL, MESSAGE_TITLE, MESSAGE_LIST, COLOR)
send_slack_message(slack_payload, SLACK_WEBHOOK_URL)