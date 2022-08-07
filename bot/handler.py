from bot.verify import verify


def handler(body):
    if not verify(body):
        return False
    