from users import dp
from aiogram import executor
from users import on_startup, on_shutdown


if __name__ == '__main__':
    print('[*] Bot pooling [*]')
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
