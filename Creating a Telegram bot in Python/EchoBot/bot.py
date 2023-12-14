import json
from telegram import Update
from telegram.ext import Updater, CallbackContext, TypeHandler


def echo(update: Update, context: CallbackContext) -> None:
    text = json.dumps(update.to_dict(), indent=2)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def main() -> None:
    updater = Updater("6341542725:AAGvWFjf7PGngQh5fPrw1gxl55AMBZdPGrM")
    updater.dispatcher.add_handler(TypeHandler(Update, echo))
    updater.start_polling()
    print('Started')
    updater.idle()

if __name__ == "__main__":
    main()