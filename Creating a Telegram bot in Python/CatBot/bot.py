import time
from telegram import bot

chat_id = 5361005636
bot = bot.Bot("6390922177:AAFgiKcViZ5pwoLzDwL4QxqvSuzjVbtSj3A")

def send_random_cat():
    url = f"https://cataas.com/cat?t=${time.time()}&"
    bot.send_photo(chat_id, url)
    
def main() -> None:
    send_random_cat()
    print('Cat has been sent. Meow!')
    
if __name__ == '__main__':
    main()