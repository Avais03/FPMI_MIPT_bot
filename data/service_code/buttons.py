from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

empty_inline_markup = InlineKeyboardMarkup()
olympiads = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="БВИ💪", callback_data="bvi"),
            InlineKeyboardButton(text="Не БВИ👌 (100 баллов)", callback_data="ne_bvi")
        ],
        [
            InlineKeyboardButton(text="ИД🏅", callback_data="achievements")
        ]
    ]
)
years = ["2021", "2020", "2019", "2018"]
olympiad = ["БВИ💪", "Не БВИ👌", "ИД🏅"]
for_FAQs = ["БВИ💪?", "ИД🏅?"]
scores = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="2021", callback_data="2021"),
            InlineKeyboardButton(text="2020", callback_data="2020")
        ],
        [
            InlineKeyboardButton(text="2019", callback_data="2019"),
            InlineKeyboardButton(text="2018", callback_data="2018")
        ]
    ]
)
for_FAQ = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="БВИ💪?", callback_data="БВИ💪?"),
        ],
        [
            InlineKeyboardButton(text="ИД🏅?", callback_data="ИД🏅?")
        ],
    ]
)
inline_markups = {"Общая информация🌞": empty_inline_markup,
                  "Программы обучения🚀": empty_inline_markup,
                  "Баллы прошлых лет👣": scores,
                  "Олимпиады🏆": olympiads,
                  "FAQ🌍": for_FAQ}
