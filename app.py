from telegram.ext import Updater, CommandHandler
import logging
import os
from comandos_telegram import *
from config import *


def run(updater):
    updater.bot.delete_webhook()

    PORT = int(os.environ.get("PORT", "8443"))
    HEROKU_APP_NAME = 'dantavs'

    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)

    updater.bot.set_webhook(url="https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TOKEN))


def define_comandos(updater):
    updater.dispatcher.add_handler(CommandHandler('hello', hello_telegram))
    updater.dispatcher.add_handler(CommandHandler('start', hello_telegram))
    updater.dispatcher.add_handler(CommandHandler('random', hello_telegram))
    updater.dispatcher.add_handler(CommandHandler('r', r_telegram))
    updater.dispatcher.add_handler(CommandHandler('c', criar_personagem_telegram))
    updater.dispatcher.add_handler(CommandHandler('ps', listar_personagens_telegram))


if __name__ == '__main__':
    TOKEN = os.getenv("TOKEN")
    mode = os.getenv("MODE")

    # Enabling logging
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logger = logging.getLogger()

    logger.info("Starting bot")

    updater = Updater(TOKEN, use_context=True)
    define_comandos(updater)

    if mode == 'dev':
        updater.bot.delete_webhook()
        updater.start_polling()
        updater.idle()
    else:
        run(updater)
