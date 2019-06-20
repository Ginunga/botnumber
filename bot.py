import requests
import telebot
from telebot.types import Message

TOKEN = "873808192:AAGJAUXVz1Rkxt0zRD5y9ytXtVhPgpmJb0c"
MAIN_URL = f"https://core.telegram.org/bots/api{TOKEN}"
r = requests.get(f"{MAIN_URL}/getUpdates")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def answer2(message: Message):
    bot.reply_to(message, "Print your number")

@bot.message_handler(commands=["all"])
def answer2(message: Message):
    bot.reply_to(message, "number.txt")

@bot.edited_message_handler(content_types=["text"])
@bot.message_handler(content_types=["text"])
def answer_1(message: Message):
    F = open("number.txt")
    K = F.read()
    if message.text in K:
        bot.reply_to(message, ">1")
    else:
        bot.reply_to(message, "Add")
        with open('number.txt', 'a') as f:
            print(message.text, file=f)

bot.polling(none_stop=True)
