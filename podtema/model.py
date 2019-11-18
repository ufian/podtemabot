# -*- coding: utf-8 -*-

__author__ = 'ufian'

import telegram_settings as config
import mongoengine as me


def get_connect():
    return me.connect(config.DB['db'], host=config.DB['host'], port=config.DB['port'], serverSelectionTimeoutMS=2500)


class Messages(me.Document):
    meta = {'collection': 'telegram'}

    date = me.DateTimeField(required=True)
    user = me.StringField()
    data = me.DictField()

