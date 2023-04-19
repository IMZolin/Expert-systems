from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_hint_inline_markup():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Подсказка: 200$', callback_data='hint'))
    return markup


def get_start_test_inline_markup():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Начать тестирование', callback_data='test'))
    return markup


def get_start_task2_inline_markup():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Задание 2', callback_data='task2'))
    return markup


def get_start_task3_inline_markup():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Задание 3', callback_data='task3'))
    return markup


def get_next_test_inline_markup():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Следующее задание', callback_data='next'))
    return markup


def get_finish_test_inline_markup():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Закончить тестирование', callback_data='finish'))
    return markup