from bot.verify import verify


def handler(body, x_line_signature):
    if not verify(body, x_line_signature):
        return False

    
    