from bot.verify import verify


users = {}


def handler(body, x_line_signature):

    # print(body['message'])
    print(body)





    if not verify(body, x_line_signature):
        return False
    
    #logic

    

    
    