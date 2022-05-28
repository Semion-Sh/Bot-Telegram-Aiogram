from create_bot import bot


async def football_poll_rafieva():
    await bot.send_poll(chat_id='-1001312541304', question='Рафиева 55, 21:30(начало)',
                        options=['Буду', 'Не буду'],
                        is_anonymous=False)

async def football_poll_ratomka():
    await bot.send_poll(chat_id='-1001312541304', question='Ратомка 21:00(начало)',
                        options=['Буду', 'Не буду'],
                        is_anonymous=False)


# -1001312541304 football chat id


async def sky_time_poll_1():
    await bot.send_poll(chat_id='-625405160', question=' Репетиция завтра в 18:00 (Четверг)',
                        options=['Буду', 'Не буду'],
                        is_anonymous=False)


async def sky_time_poll_2():
    await bot.send_poll(chat_id='-625405160', question='Репетиция завтра в 19:30 (Суббота)',
                        options=['Буду', 'Не буду'],
                        is_anonymous=False)
# -1001323540103