import os

from dotenv import load_dotenv

from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update


load_dotenv()


def start(update: Update, context: CallbackContext):
    bot = context.bot

    bot.send_message(
        chat_id=update.message.chat.id,
        text='salom botga xush kelibsiz.'
    )


def echo(update: Update, context: CallbackContext):
    bot = context.bot

    bot.send_message(
        chat_id=update.message.chat.id,
        text=update.message.text
    )


def main() -> None:
    updater = Updater(os.getenv('TOKEN'))
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()


main()
