import os

from dotenv import load_dotenv

from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    Filters,
)
from telegram import Update


load_dotenv()


def start(update: Update, context: CallbackContext):
    update.message.reply_text(text="Assalomu alaykum!")


def randomcat(update: Update, context: CallbackContext):
    update.message.reply_photo(photo="https://cataas.com/cat")


def greet(update: Update, context: CallbackContext):
    command, name = update.message.text.split(" ")
    update.message.reply_text(f"salom {name}")


def calc(update: Update, context: CallbackContext):
    command, operand01, operator, operand02 = update.message.text.split(
        " "
    )  # "/calc 8 + 6" -> ["/calc", "8", "+", "6"]

    result = "xatolik berdi"
    if operator == "+":
        result = str(int(operand01) + int(operand02))
    if operator == "-":
        result = str(int(operand01) - int(operand02))
    if operator == "*":
        result = str(int(operand01) * int(operand02))
    if operator == "/":
        if int(operand02) == 0:
            result = "nolga bolish mumkin emas"
        else:
            result = str(int(operand01) / int(operand02))

    update.message.reply_text(result)


def echo(update: Update, context: CallbackContext):
    update.message.reply_text(text=update.message.text)


def main() -> None:
    updater = Updater(os.getenv("TOKEN"))
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("randomcat", randomcat))
    dispatcher.add_handler(CommandHandler("greet", greet))
    dispatcher.add_handler(CommandHandler("calc", calc))  # /calc 3 + 5

    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()


main()