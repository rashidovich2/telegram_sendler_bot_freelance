from environs import Env
from random import choice

env = Env()

env.read_env(override=True)

api_id = env.int('api_id')
api_hash = env.str('api_hash')
BOT_TOKEN = env.str('BOT_TOKEN')


