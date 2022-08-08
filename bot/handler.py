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

    user_id = body['events'][0]['source']['userId']
    reply_token = body['events'][0]['replyToken']
    type_ = body['events'][0]['message']['type']
    if not user_id in users.keys():
        msg = body['events'][0]['message']['text']
        if type_ == 'text' and msg.lower() == '/register':  
            line_bot_api.reply_message(reply_token, TextSendMessage(text='OK. We are about to start a short registration process...'))
            users[user_id] = 1
        else:
            line_bot_api.reply_message(reply_token, TextSendMessage(text='Please, press the "Registration" button to register'))
    # if not verify(body, x_line_signature):
    #     return False
    
    #logic
    
    
    
    if users[user_id] == 1:
        if type_ != 'text':
            line_bot_api.reply_message(reply_token, TextSendMessage(text='Please tell use your full name'))
        elif user_id in users.keys():
            name = body['events'][0]['message']['text']
            if not ' ' in name or len(name.split(' ')) != 2:
                line_bot_api.reply_message(reply_token, TextSendMessage(text='Please tell use your full name'))
            else:
                line_bot_api.reply_message(reply_token, TextSendMessage(text=f'Thank you! It is nice to meet you {name}!\n\nTo finish the registration, please share your home location.'))
                users[user_id] += 1
    
    elif users[user_id] == 2:
        if type_ != 'location':
            line_bot_api.reply_message(reply_token, TextSendMessage(text='Please share your home location'))
        elif user_id in users.keys():
            address = body['events'][0]['message']['address']
            line_bot_api.reply_message(reply_token, TextSendMessage(text=f'Thank you! Now we now where you live... Good luck!\n{address}'))
            line_bot_api.reply_message(reply_token, TextSendMessage(text='Registration finished!'))

        
    

    
    