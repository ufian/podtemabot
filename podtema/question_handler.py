# -*- coding: utf-8 -*-

import datetime as dt
import re

from podtema.model import Messages

QUESTION_PATTERN = re.compile(r'(\w{2,})\?')

def handler(msg):
    text = msg['text'].strip()
    msg_from = msg['from']
    user = msg_from.get('username', msg_from.get('first_name'))

    words = QUESTION_PATTERN.findall(text)

    if not words:
        return "Непонятно без вопроса"

    if Messages.objects(user=user, date__gt=dt.datetime.now() - dt.timedelta(days=1)).count() >= 3:
        return "Хватит, @{0}, присылать вопросы. Татарин советует вернуться завтра.".format(user)

    m = Messages(
        date=dt.datetime.now(),
        user=user,
        data=msg
    )
    m.save()

    return "Принято! Большое Татарское спасибо"