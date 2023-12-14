import re
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, Filters, MessageHandler, BaseFilter

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("""
    Бот может здороваться на разных языках.
    Список поддерживаемых приветствий:
    - привет - русский
    - hello - английский
    - hola - испанский
    """)
    
def ru (update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет!")
    
def en (update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello!")
    
def es (update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hola!")
    
def unknown_lagn (update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Приветстствие {update.message.text} не поддерживается.')
    
def get_greeting_filter (greeting: str) -> BaseFilter:
    return Filters.regex(re.compile(f"^{greeting}$", re.IGNORECASE)) & Filters.update.message

def main():
    updater = Updater("6302930510:AAEeQrJq7J5aw8xW7pDxDwKQ1K9wFK9TZs8")
    updater.dispatcher.add_handler(CommandHandler("help", help_command))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter("привет"), ru))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter("hello"), en))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter("hola"), es))
    updater.dispatcher.add_handler(MessageHandler(Filters.update.message & Filters.text, unknown_lagn))
    updater.start_polling()
    print("Started")
    updater.idle()
    
if __name__ == "__main__":
    main()