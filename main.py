import os

from dotenv import load_dotenv

from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update


load_dotenv()


def start(update: Update, context: CallbackContext):
    update.message.reply_text(text='Assalomu alaykum!')


def echo(update: Update, context: CallbackContext):
    update.message.reply_text(text=update.message.text)


def main() -> None:
    updater = Updater(os.getenv('TOKEN'))
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()


main()
