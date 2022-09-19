from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData

# post_callback = CallbackData("create_post", "action")
#
# conf_key = InlineKeyboardMarkup(
#         inline_keyboard=[
#             [
#                 InlineKeyboardButton(text="Подтвердить", callback_data=post_callback.new(action="yes")),
#                 InlineKeyboardButton(text="Отмена", callback_data=post_callback.new(action="no"))
#
#
#                 ]
#             ]
#         )

conf_key = ReplyKeyboardMarkup(resize_keyboard=True)
conf_key.add(KeyboardButton(text="Подтвердить"), KeyboardButton(text='Отмена'))
