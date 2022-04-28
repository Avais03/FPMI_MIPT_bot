import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

print(config.bot_started)


@bot.message_handler(commands=['start'])
def opa(message):
    # bot.send_message(message.chat.id, '<b>Ты хуле тут делаешь?</b>', parse_mode='html')
    # for keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item0 = types.KeyboardButton("Общая информация🌞")
    item1 = types.KeyboardButton("Программы обучения🚀")
    item2 = types.KeyboardButton("Баллы прошлых лет👣")
    item3 = types.KeyboardButton("Олимпиады🏆")
    item4 = types.KeyboardButton("FAQ🌍")
    markup.add(item0, item1, item4, item3, item2)

    # send greeting
    bot.send_message(message.chat.id,
                     config.greeting.format(message.from_user, bot.get_me()),
                     parse_mode='html')

    # send sticker
    sticker = open('data/static/Potential.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker, reply_markup=markup)


@bot.message_handler()
def text_from_user(messages):
    bot.send_message(messages.chat.id, messages, parse_mode='html')


# @bot.message_handler(content_types=['text'])
# def main_menu(message):
#     if message.chat.type == 'private':
#         if message.text == "Баллы прошлых лет👣":
#             bot.send_message(message.chat.id, config.FPMI_message, parse_mode='html')
#         elif message.text == "Олимпиады🏆":
#
#         elif message.text == "Общая информация🌞":
#         elif message.text == "FAQ🌍":
#         elif message.text == "Программы обучения🚀":


bot.polling(none_stop=True)
