# -*- coding: utf-8 -*-

__author__ = 'ufian'

import time

import telepot
from telepot.loop import MessageLoop

import telegram_settings as config
from podtema.question_handler import handler as question_hander
from podtema.model import get_connect


bot = telepot.Bot(config.TOKEN)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        if msg['text'].startswith("/start"):
            bot.sendMessage(chat_id, "Задайте вопрос и знак вопроса не забудьте")
            return

        reply = question_hander(msg)

        if reply is not None:
            bot.sendMessage(chat_id, reply)

get_connect()
MessageLoop(bot, handle).run_as_thread()

print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)