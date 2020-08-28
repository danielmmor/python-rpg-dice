# -*- coding: utf-8 -*-
from bot import telegram_dadobot
from rpg import rolagem

bot = telegram_dadobot("config.cfg")

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates['result']
    if updates:
        for item in updates:
            update_id = item['update_id']
            try:
                message = str(item['message']['text'])
                reply_to = str(item['message']['message_id'])
            except:
                message = None
            from_ = item['message']['chat']['id']
            try:
                if message.find('/') != -1:
                    reply = rolagem(message)
                    bot.send_message(reply, from_, reply_to)
                    print(reply, from_, reply_to)
            except:
                deu_ruim = None
