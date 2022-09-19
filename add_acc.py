import asyncio
from pyrogram import Client
from pyrogram.raw.functions.account import GetAuthorizations
from database import insert_data_account


def reg_account():
    name = input('\nВведите имя(на английском): ')
    api_id = input('\nВведите api_id(telegram.org): ')
    api_hash = input('\nВведите api_hash(telegram.org): ')
    with Client(name=name, api_id=int(api_id), api_hash=api_hash) as app:
        insert_data_account(int(api_id), str(api_hash), str(name), 1)
        print('Account added')


reg_account()
