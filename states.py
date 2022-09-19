from aiogram.dispatcher.filters.state import StatesGroup, State

class Text(StatesGroup):
    answer1 = State()
    answer2 = State()
