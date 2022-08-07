
import requests
from bot.verify import TOKEN, root, SECRET
import os
import json
richmenu_id = '0'

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


# data = {
#     "size": {
#       "width": 2500,
#       "height": 1686
#     },
#     "selected": False,
#     "name": "Nice richmenu",
#     "chatBarText": "Tap here",
#     "areas": [
#       {
#         "bounds": {
#           "x": 0,
#           "y": 0,
#           "width": 2500,
#           "height": 1686
#         },
#         "action": {
#           "type": "postback",
#           "data": "action=buy&itemid=123"
#         }
#       }
#    ]
# }
# 
# data = json.dumps(data)
# r = requests.post(f'https://api.line.me/v2/bot/richmenu', 
#                     data=data,
#                     headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {TOKEN}'})


# print(r)


line_bot_api = LineBotApi(TOKEN)
handler = WebhookHandler(SECRET)



image = os.path.join(root, 'register.png')
file = open(image, 'rb')
with open(image, 'rb') as f:
    print(line_bot_api.set_rich_menu_image(richmenu_id, 'image/png', f))
# r = requests.post(f'https://api-data.line.me/v2/bot/richmenu/{richmenu_id}/content', 
#                     files={'media': file},
#                     headers={'Content-Type': 'image/png', 'Authorization': f'Bearer {TOKEN}'})


print(r)



# r = requests.post(f'https://api.line.me/v2/bot/user/all/richmenu/{richmenu_id}', 
#                     headers={'Content-Type': 'image/png', 'Authorization': f'Bearer {TOKEN}'})


# print(r)