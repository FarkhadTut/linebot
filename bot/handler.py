from bot.verify import verify


users = {}


def handler(body, x_line_signature):

    # print(body['message'])





    if not verify(body, x_line_signature):
        return False
    
    #logic

    

    
    