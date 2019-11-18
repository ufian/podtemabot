# -*- coding: utf-8 -*-

import datetime as dt

from podtema.model import Messages


def handler(msg):
    text = msg['text'].strip()
    msg_from = msg['from']
    user = msg_from.get('username', msg_from.get('first_name'))

    if not text.endswith("?"):
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