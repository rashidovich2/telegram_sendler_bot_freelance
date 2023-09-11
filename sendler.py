import sqlite3
from database import select_all_acc, select_flag_acc
from dispatcher import bot

import asyncio
from pyrogram import client

from pyrogram.errors.exceptions.flood_420 import FloodWait
from aiogram.dispatcher import FSMContext
from data import MainDatabase

from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired, PeerFlood, InputUserDeactivated
from random import randint, choice

database = MainDatabase("users.db")
"""info_user = [[15307593, 'd04664e046c374176fad7488eaefb67d', 'acc', 'St'],
             [14045568, '145af0e94fbc93dc3a0b031d254e1914', 'accot2', 'Трофим'],
             [18979205, '145af0e94fbc93dc3a0b031d254e1914', 'accot3', 'Степан'],
             [9511956, 'd67965b1cf3c6e0d1a7e918d69d6514c', 'accot4', 'Филат'],
             [9100549, 'aa73030b483024de4418a375e4ca888f', 'accot5', 'Тимур'],
             [17082843, 'ece3dd727ae5b8cb7d400dfdd25d789e', 'accot6', 'Георгий'],
             [17837556, 'ed49031a27ad5865c552a1cda6c3ef61', 'accot7', 'Светлана'],
             [13992446, 'f4b482b8ef4f10fae77abd4339404bc2', 'accot8', 'Роман'],
             [17878978, '6e74d39c3d138289b039d3dbce9e9582', 'accot9', 'Роман'],
             [16557614, '508575622949b942c92729b181288435', 'accot10', 'Кирилл'],
             [11176781, '22b3c915c31809203a6fba4350bd30b7', 'accot11', 'Руслан'],
             [18310871, 'aca14b834baa6f44ea6841dea6fb292c', 'accot12', 'Семен'],
             [10499356, 'aecb58c62d27ee59fc5a660547fcdc01', 'accot13', 'Ярослав'],
             [10317787, '3d5f393d9a98042e9ef19731282aaa19', 'accot14', 'Олег'],
             [13010540, '96c2b4533e40655ba50704945fd6a5c3', 'accot15', 'Николай'],
             [13532642, 'e6fd1663c3a039823c249ca91e276ea0', 'accot16', 'Аркадий'],
             [10754175, '56c657dda400b6784369556ab3ee68d7', 'accot17', 'Савва'],
             [19863811, 'afa317f682666862d561f57f2da51159', 'accot18', 'Харитон'],
             [10254535, 'f1d429e86dc69172a94c5cb039143125', 'accot19', 'Марк']
             ]"""

info_user_db = select_all_acc()
check_status = {i[1]: i[4] for i in info_user_db}
class Variable:
    api_id = info_user_db[-1][1]
    api_hash = info_user_db[-1][2]
    name = info_user_db[-1][3]
    flag = 1


async def sendler(name, _id, _hash, text):
    async with client.Client(name, _id, _hash) as app:
        name = await app.get_users("me")
        await bot.send_message(chat_id=5085656302, text=f"Рассылка началась с аккаунта '{name.first_name}'")
        check_status[Variable.api_id] = 1
        async for dialog in app.get_dialogs():
            await asyncio.sleep(5)
            if dialog.chat.title is not None:
                try:
                    async for member in app.get_chat_members(dialog.chat.id):
                        count = await app.search_messages_count(chat_id=member.user.id)
                        if database.get_user(member.user.id) is not None:
                            await asyncio.sleep(2)
                            print('Continue 1')
                            continue
                        if count >= 1:
                            if database.get_user(member.user.id) is not None:
                                await asyncio.sleep(2)
                                print('Continue 2')
                                continue

                            else:
                                database.add_user(member.user.id)
                                await asyncio.sleep(2)
                                print('Continue 3')
                                continue

                        else:
                            if member.user.is_bot:
                                await asyncio.sleep(2)
                                print('Continue 4')
                                continue

                            else:
                                database.add_user(member.user.id)
                                try:
                                    await app.send_message(chat_id=member.user.id, text=text)
                                    print('message send')
                                    await asyncio.sleep(randint(20, 120))
                                except PeerFlood:
                                    check_status[Variable.api_id] = 0
                                    ins = []
                                    users_not_spam = []
                                    for acc in info_user_db:
                                        if check_status[acc[1]]:
                                            print(f'acc append {acc[1]}')
                                            ins.append(
                                                [acc[1], acc[2], acc[3]])
                                            users_not_spam.append(acc[3])
                                        else:
                                            print(
                                                f'acc block {acc[1], check_status[acc[1]]}')

                                    print(
                                        f'Аккаунты не в спаме: {users_not_spam}')
                                    new_info = choice(ins)
                                    await bot.send_message(chat_id=5085656302,
                                                           text=f"Бот переключился на аккаунт '{new_info[0]}', запустите рассылку\n"
                                                           f"Аккаунты не в спаме: {users_not_spam}")
                                    print(check_status)
                                    _id = new_info[0]
                                    _hash = new_info[1]
                                    name = new_info[2]

                                    try:
                                        await sendler(name, _id, _hash, text)
                                        if not ins:
                                            print('Нет акков не в спаме')
                                            ins = info_user_db
                                            return
                                    except:
                                        await sendler(name, _id, _hash, text)
                        # print(f'{member.user.first_name} = {await app.search_messages_count(chat_id=member.user.id)}')

                except ChatAdminRequired as error:
                    pass
                except InputUserDeactivated as error:
                    pass
                except FloodWait:
                    print("Flood Wait")
                    await asyncio.sleep(300)


async def send_all_message(text, flag=True):
    i = 0
    print(Variable.api_id, Variable.api_hash, Variable.name)
    Variable.flag = True
    await sendler(Variable.name, Variable.api_id, Variable.api_hash, text=text)
