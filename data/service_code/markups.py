import aiogram
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b_Main = KeyboardButton('◀️ Меню')
stack_of_parents = []


class SubMenu:
    names_buttons_ = []
    buttons_ = []
    markup_ = ReplyKeyboardMarkup(resize_keyboard=True).add(*buttons_)

    def build_markup(self):
        self.buttons_ = [KeyboardButton(name) for name in self.names_buttons_]
        self.markup_ = ReplyKeyboardMarkup(resize_keyboard=True).add(*self.buttons_, b_Main)


# --- Main Menu ---
mainMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Общая информация🌞"),
            KeyboardButton(text="Программы обучения🚀"),
        ],
        [
            KeyboardButton(text="Баллы прошлых лет👣"),
            KeyboardButton(text="Олимпиады🏆"),
            KeyboardButton(text="FAQ🌍"),
        ],
    ],
    resize_keyboard=True
)

# names_buttons_menu = ["Общая информация🌞", "Программы обучения🚀", "Баллы прошлых лет👣", "Олимпиады🏆", "FAQ🌍"]
# buttons = [KeyboardButton(name) for name in names_buttons_menu]
# mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(*buttons)

# # --- Олимпиады🏆 ---
# olympiads_markup = SubMenu()
# olympiads_markup.names_buttons_ = ["БВИ💪", "Не БВИ👌", "ИД🏅"]
# olympiads_markup.build_markup()
#
# # --- "Баллы прошлых лет👣" ---
# scores = SubMenu()
# scores.names_buttons_ = ["2020", "2021"]
# scores.build_markup()


def except_markup():
    markup = aiogram.types.InlineKeyboardMarkup()
    item = aiogram.types.InlineKeyboardButton("Предложить!")
    markup.add(item)
