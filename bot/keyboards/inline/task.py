from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_hint_inline_markup():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Подсказка: 200$', callback_data='hint'))
    return markup