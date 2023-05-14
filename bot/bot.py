import telebot
import requests
from telebot import types
base_url = "http://127.0.0.1:8000/api"
bot = telebot.TeleBot("5990485431:AAESCgCr5-hlIxktBwgRN-t0ln20FI5aI44")


markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
markup.add(types.KeyboardButton('listening🎧'), types.KeyboardButton('reading📚'), types.KeyboardButton('speaking🗣'), types.KeyboardButton('writing✍'), )


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    try:
        text = requests.get(f"{base_url}/bot-info/").json()
        print(text)
        bot.send_message(message.from_user.id, text['text'], reply_markup=markup)
    except Exception as err:
        bot.send_message(message.from_user.id, 'Welcome to our bot', reply_markup=markup)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    try:
        if message.text == 'listening🎧':
            query = requests.get(f'{base_url}/listening/').json()
            print(query)
            text = f"<b>From your search</b>\n{query['about']}\nsource: <b>{query['source']}</b>"
            bot.send_photo(message.from_user.id, 'https://ieltsmaterial.com/images/theme/category/listening.jpg', text, reply_markup=markup, parse_mode='HTML')
        elif message.text == 'reading📚':
            query = requests.get(f'{base_url}/reading/').json()
            print(query)
            text = f"<b>From your search</b>\n{query['about']}\nsource: <b>{query['source']}</b>"
            bot.send_photo(message.from_user.id, 'https://ieltsmaterial.com/images/theme/category/reading.jpg',text, reply_markup=markup, parse_mode='HTML')
        elif message.text == 'speaking🗣':
            query = requests.get(f'{base_url}/speaking/').json()
            print(query)
            text = f"<b>From your search</b>\n{query['about']}\nsource: <b>{query['source']}</b>"
            bot.send_photo(message.from_user.id, 'https://ieltsmaterial.com/images/theme/category/speaking.jpg', text, reply_markup=markup, parse_mode='HTML')
        elif message.text == 'writing✍':
            query = requests.get(f'{base_url}/writing/').json()
            print(query)
            text = f"<b>From your search</b>\n{query['about']}\nsource: <b>{query['source']}</b>"
            bot.send_photo(message.from_user.id, 'https://ieltsmaterial.com/images/theme/category/writing.jpg', text, reply_markup=markup, parse_mode='HTML')

        else:
            bot.reply_to(message, message.text)
    except Exception as err:
        print(err)


bot.infinity_polling()
