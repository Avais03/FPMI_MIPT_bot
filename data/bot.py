import aiogram
import logging
import service_code.config

from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from service_code import buttons as but
from service_code import descriptions as desc
from service_code import markups as mkps

# log level
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    )
print(service_code.config.bot_started)

# bot init
bot = aiogram.Bot(token=service_code.config.TOKEN)
dp = aiogram.Dispatcher(bot)
guest = ''
quest_action = ''


@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    # bot.send_message(message.chat.id, '<b>Ты че тут делаешь?</b>', parse_mode='html')
    global guest
    guest = message.from_user.mention
    # send greeting
    await message.answer(desc.greeting1.format(message.from_user), parse_mode='html')
    # send sticker
    sticker = open('static/Potential.webp', 'rb')
    await bot.send_sticker(message.chat.id, sticker, reply_markup=mkps.mainMenu)
    await bot.send_message(chat_id=service_code.config.admin_id, text=f"{message.from_user.mention} - {message.text}")


@dp.message_handler(Text(equals=["Общая информация🌞", "Программы обучения🚀",
                                 "Баллы прошлых лет👣", "Олимпиады🏆", "FAQ🌍"]))
async def get_click(message: Message):
    # send answer on menu click
    global guest
    guest = message.from_user.mention
    await message.answer(desc.menu_descriptions[message.text], reply_markup=but.inline_markups[message.text],
                         parse_mode='Markdown')
    await bot.send_message(chat_id=service_code.config.admin_id, text=f"{message.from_user.mention} - {message.text}")


@dp.callback_query_handler(
    Text(equals=["bvi", "ne_bvi", "achievements", "2021", "2020", "2019", "2018", "БВИ💪?", "ИД🏅?"]))
async def for_bvi(call: CallbackQuery):
    callback_data = call.data
    await call.message.answer(desc.button_descriptions[callback_data], parse_mode="html")
    await bot.send_message(chat_id=service_code.config.admin_id,
                           text=f"{guest} - {callback_data}")


# run long-polling
if __name__ == "__main__":
    aiogram.executor.start_polling(dp, skip_updates=False)
