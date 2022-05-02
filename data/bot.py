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


@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    # bot.send_message(message.chat.id, '<b>Ты че тут делаешь?</b>', parse_mode='html')

    # send greeting
    await message.answer(desc.greeting1.format(message.from_user),
                         parse_mode='html')
    # send sticker
    sticker = open('static/Potential.webp', 'rb')
    await bot.send_sticker(message.chat.id, sticker, reply_markup=mkps.mainMenu)


@dp.message_handler(Text(equals=["Общая информация🌞", "Программы обучения🚀",
                                 "Баллы прошлых лет👣", "Олимпиады🏆", "FAQ🌍"]))
async def get_click(message: Message):
    await message.answer(desc.menu_descriptions[message.text], reply_markup=but.inline_markups[message.text],
                         parse_mode='Markdown')


# @dp.callback_query_handlers(service_code.button_processing.olympiads.filter(item_name=))
# @dp.message_handler(Command("items"))
# async def show_items(message : Message):
#     await message.answer(reply_markup=choise)

@dp.callback_query_handler(text_contains="bvi")
async def for_bvi(message: Message):
    await bot.send_message(message.from_user.id, desc.bvi)


@dp.callback_query_handler(text_contains="ne_bvi")
async def for_bvi(message: Message):
    await bot.send_message(message.from_user.id, desc.ne_bvi)


@dp.callback_query_handler(text_contains="achievements")
async def for_bvi(message: Message):
    await bot.send_message(message.from_user.id, desc.achievements)


@dp.callback_query_handler(text_contains="2021")
async def for_bvi(message: Message):
    await bot.send_message(message.from_user.id, desc.year_2021)


@dp.callback_query_handler(text_contains="2020")
async def for_bvi(message: Message):
    await bot.send_message(message.from_user.id, desc.year_2020)


@dp.callback_query_handler(text_contains="2019")
async def for_bvi(message: Message):
    await bot.send_message(message.from_user.id, desc.year_2019)


@dp.callback_query_handler(text_contains="2018")
async def for_bvi(message: Message):
    await bot.send_message(message.from_user.id, desc.year_2018)


@dp.callback_query_handler(text_contains="БВИ💪?")
async def for_bvi(message: Message):
    await bot.send_message(message.from_user.id, "Ну БВИ, так БВИ")


@dp.callback_query_handler(text_contains="ИД🏅?")
async def for_bvi(message: Message):
    await bot.send_message(message.from_user.id, "Ну ИД, так ИД.")


# run long-polling
if __name__ == "__main__":
    aiogram.executor.start_polling(dp, skip_updates=True)
