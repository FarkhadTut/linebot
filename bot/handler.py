from bot.verify import verify, TOKEN, root, SECRET
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

line_bot_api = LineBotApi(TOKEN)
handler = WebhookHandler(SECRET)
users = {}


def handler(body, x_line_signature):

    # print(body['message'])

    user_id = body['events'][0]['message']['source']['userId']
    reply_token = body['events'][0]['replyToken']

    if not user_id in users.keys():
        users[user_id] = 1
    # if not verify(body, x_line_signature):
    #     return False
    
    #logic
    type_ = body['events'][0]['message']['type']
    
    
    if users[user_id] == 1:
        if type_ != 'text':
            line_bot_api.reply_message(reply_token, TextSendMessage(text='Please tell use your full name'))
        elif user_id in users.keys():
            name = body['events'][0]['message']['text']
            line_bot_api.reply_message(reply_token, TextSendMessage(text=f'Thank you! It is nice to meet you {name}!\nTo finish the registration, please share your home location.'))
            users[user_id] += 1
    
    elif users[user_id] == 2:
        if type_ != 'location':
            line_bot_api.reply_message(reply_token, TextSendMessage(text='Please share your home location'))
        elif user_id in users.keys():
            address = body['events'][0]['message']['address']
            line_bot_api.reply_message(reply_token, TextSendMessage(text=f'Thank you! Now we now where you live... Good luck!\n{address}'))

        
    

    
    