import logging, sys
from bot import bot
from kernel import config
from database import create_table

logging.basicConfig(level = logging.WARNING, format = '[%(asctime)s] [%(filename)s %(levelname)s] %(message)s', datefmt='%y-%m-%d %H:%M:%S', handlers = [logging.FileHandler("logs.log"), logging.StreamHandler(sys.stdout)] )


@bot.event
async def on_ready():
    create_table.start()
    print(f"Бот успешно запустился под аккаунтом {bot.user}\n{'*' * 50}")


if __name__ == '__main__':
    bot.run(config.bot.token)