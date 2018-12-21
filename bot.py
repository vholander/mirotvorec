# -*- coding: utf-8 -*-
import redis
import os
import telebot
# import some_api_lib
# import ...

# Example of your code beginning
bot = telebot.TeleBot('653745692:AAGZgPfeePUrQTd6-MrRwQRLo9jL0WtTmBs', threaded=False)


def default_test(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site1 = types.InlineKeyboardButton(text='перевірити вказану особу по Миротворцю', url='https://myrotvorets.center/criminal/?cf[name]='+ message.text )
    markup.row(btn_my_site1)
    bot.send_message(message.chat.id, message.text, reply_markup=markup)






@bot.message_handler(content_types=['text'])
def handle_text(message):
        default_test(message)



while True:
    try:
        bot.infinity_polling(True)
    except Exception as err:
        print("eroor")
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
some_api_token = os.environ['SOME_API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
# bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...
