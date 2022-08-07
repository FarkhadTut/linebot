from bot.verify import verify


def handler(body, x_line_signature):
    print(verify(body, x_line_signature))
    print(body)
    if not verify(body, x_line_signature):
        return False

    
    