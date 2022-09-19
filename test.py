import asyncio
from pyrogram import Client
from pyrogram.raw.functions.account import GetAuthorizations

"""with Client(name='accot20', api_id=11627825, api_hash='38f89b14a9997813b257cda31f66076f', phone_number='+79652365363') as app:
    name = app.get_users('me')
    print(name)"""

def reg_account():
    name = input('Введите имя(на английском): ')
    api_id = input('Введите api_id(telegram.org): ')
    api_hash = input('Введите api_hash(telegram.org): ')
    with Client(name=name, api_id=int(api_id), api_hash=api_hash) as app:
        name = app.get_users('me')
        print(name)


reg_account()