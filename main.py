import json

from slack import WebClient


SLACK_BOT_TOKEN = "xoxb-5196651609927-5212228521443-rk1dTVe3OG1WzfTM1vZp0yHw"
app = WebClient(token=SLACK_BOT_TOKEN)
# response = client.chat_postMessage(channel="#test_bot", text="Hello World!!!")
def hello():
    return "oo"
# blocks = [
#         {"type": "section",
#          "text": {"type": "mrkdwn",
#                 "text": f"Hello! What you want do?"}
#         },
#         {"type": "actions",
#          "elements": [{"type": "button",
#                        "text": {"type": "plain_text",
#                                 "text": "command 1",
#                     },
#                     "value": "command1",
#                 },
#                 {
#                     "type": "button",
#                     "text": {
#                         "type": "plain_text",
#                         "text": "command 2"
#                     },
#                     "value": "command2"
#                 },
#                 {
#                     "type": "button",
#                     "text": {
#                         "type": "plain_text",
#                         "text": "command 3"
#                     },
#                     "value": "command3"
#                 }
#             ]
#         }
#     ]
hello_message = "I want to live! Please build me."
message_attachments = [
            {
                "pretext": "I'll tell you how to set up your system. :robot_face:",
                "text": "What operating system are you using?",
                "callback_id": "os",
                "color": "#3AA3E3",
                "attachment_type": "default",
                "actions": [
                    {
                        "name": "Command1",
                        "text": "Command_1",
                        "type": "button",
                        "value": "value_1"
                    },
                    {
                        "name": "Command2",
                        "text": "Command_2",
                        "type": "button",
                        "value": "value_2",
                        "confirm": {
                            "title": "Are you sure?",
                            "text": "Are you sure what you want Сommand_2?",
                            "ok_text": "Yes",
                            "dismiss_text": "No"
                        }
                    }
                ]
            }
        ]
response = app.chat_postMessage(channel="#test_bot", test=hello_message, attachments=json.dumps(message_attachments))
print(response)



