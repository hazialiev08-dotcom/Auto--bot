
import telebot
import os
from telebot import types

TELEGRAM_TOKEN = os.environ.get('BOT_TOKEN')
ADMIN_ID = int(os.environ.get('ADMIN_ID', 0))

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton("Продать авто"),
        types.KeyboardButton("Узнать стоимость"),
        types.KeyboardButton("Связаться с экспертом"),
        types.KeyboardButton("Помощь")
    )
    return markup

def notify_admin(username, text):
    if ADMIN_ID and ADMIN_ID != 0:
        try:
            msg = "Новая заявка!\n\n@" + str(username) + "\nТекст: " + str(text)
            bot.send_message(ADMIN_ID, msg)
        except Exception as e:
            print("Ошибка: " + str(e))

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Здравствуйте! Я бот для выкупа авто. Выберите действие:", reply_markup=main_menu())

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "Напишите о вашем авто.", reply_markup=main_menu())

@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text
    if text == "Продать авто":
        bot.send_message(message.chat.id, "Напишите марку и год.")
        return
    if text == "Узнать стоимость":
        bot.send_message(message.chat.id, "Напишите марку и пробег.")
        return
    if text == "Связаться с экспертом":
        bot.send_message(message.chat.id, "Оставьте номер телефона.")
        return
    if text == "Помощь":
        help_message(message)
        return
    username = message.from_user.username or "id" + str(message.chat.id)
    notify_admin(username, text)
    bot.send_message(message.chat.id, "Спасибо! Заявка принята.")

print("Бот запущен...")
while True:
    try:
        bot.polling(none_stop=True, timeout=60)
    except Exception as e:
        print("Переподключение...")
        import time
        time.sleep(5)
