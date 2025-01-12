import os
import json
import sys
import requests

SLACK_WEBHOOK_URL = os.getenv('slack-webhook-url')
ACTOR = os.getenv('actor', 'ghkdqhrbals')
ACTOR_PROFILE_URL = f'https://github.com/{ACTOR}'
MESSAGE_LIST = json.loads(os.getenv('messages'))
MESSAGE_TITLE = os.getenv('message-title', 'Slack Alert List')
COLOR = os.getenv('color', '#3bb143')  # 색상을 환경 변수에서 읽어오며 기본값은 #3bb143

def build_slack_payload(actor, actor_profile_url, message_title, message_list, color):
    # Attachments 구성
    attachments = [
        {
            "color": color,  # 외부에서 전달받은 색상
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "\n".join([f"• {module}" for module in message_list])
                    }
                }
            ]
        }
    ]

    return {
        "username": "Slack Bot",  # 슬랙 메시지를 보내는 사용자 이름
        "icon_emoji": ":robot_face:",  # 메시지 아이콘
        "text": f"{message_title} ( by <{actor_profile_url}|{actor}> )",  # 메시지 상단에 표시될 텍스트
        "attachments": attachments  # Attachments를 payload에 포함
    }

def send_slack_message(payload):
    response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
    if response.status_code == 200:
        print("Slack message sent successfully.")
    else:
        print(f"Failed to send Slack message. Status code: {response.status_code}, Response: {response.text}")
        sys.exit(1)

# Payload 생성 및 메시지 전송
slack_payload = build_slack_payload(ACTOR, ACTOR_PROFILE_URL, MESSAGE_TITLE, MESSAGE_LIST, COLOR)
send_slack_message(slack_payload)