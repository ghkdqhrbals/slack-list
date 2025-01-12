# Alert to slack with lists of messages

# Slack Send List GitHub Action

Send list of data into Slack!

## Setup variables

```yaml
- name: Send GitHub Action trigger data to Slack workflow
  id: slack
  uses: ghkdqhrbals/slack-list@v1.0.3
  with:
    SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
    actor: ${{ github.actor }}
    messages: '["test1", "test2", "test3"]'
    message-title: 'Testing Slack Notification Header'
    color: '#3bb143'
```

And will get the following message in Slack:

![img.png](img.png)
