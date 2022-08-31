# #  Telegram BOT
# function to send message to group or private messege
async def sendMassage(msg, session):
    token = "your telegram token"
    chatID = "your chat id on telegram "
    params = {"chat_id":chatID,"text":msg}
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    async with session.get(url, params=params, timeout=30) as r:
        pass
