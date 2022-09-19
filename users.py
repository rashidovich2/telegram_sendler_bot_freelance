import asyncio
import sqlite3
from database import select_all_acc

from dispatcher import dp, bot
from random import choice

from aiogram import types
from aiogram.dispatcher import FSMContext

from states import Text
from sendler import send_all_message

from keyboard.inline import conf_key
from sendler import Variable

from aiogram.dispatcher import filters

loop = asyncio.get_event_loop()


async def on_startup(_):
    user_id = 5085656302
    await bot.send_message(user_id, 'Бот запущен')


async def on_shutdown(_):
    user_id = 5085656302
    await bot.send_message(user_id, 'Бот выключен')


@dp.message_handler(commands=['start_sends'], state=None)
async def start_send(msg: types.Message):
    # print(msg.from_user.id)
    await msg.answer("Отправьте текст для рассылки.")
    await Text.answer1.set()


@dp.message_handler(state=Text.answer1)
async def answer1(msg: types.Message, state: FSMContext):
    await state.update_data(text=msg.html_text)
    await msg.answer("Подтвердите действие", reply_markup=conf_key)
    await Text.answer2.set()


@dp.message_handler(filters.Text(equals="Подтвердить"), state=Text.answer2)
async def answer2_yes(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer("Вы отменили действие", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(filters.Text(equals="Отмена"), state=Text.answer2)
async def answer2_yes(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        dates = data.get('text')
    with sqlite3.connect("check.db") as sqlite:
        cursor = sqlite.cursor()
        cursor.execute("""Update valbul set value = True""")
        sqlite.commit()
    await msg.answer("Рассылка началась.", reply_markup=types.ReplyKeyboardRemove())
    print(dates)
    await state.finish()
    loop.create_task(send_all_message(text=dates))


@dp.message_handler(commands=['stop_sends'])
async def stop_sends(msg: types.Message):
    await msg.answer("Рассылка остановлена.")
    with sqlite3.connect("/root/Send_message_to_user/check.db") as sqlite:
        cursor = sqlite.cursor()
        cursor.execute("""Update valbul set value = False""")
        sqlite.commit()
