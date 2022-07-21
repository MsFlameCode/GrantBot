from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


def create_keyboard_common():
    button = KeyboardButton('Конкурсы', callback_data='contests')
    markup = ReplyKeyboardMarkup(resize_keyboard=True).row(button)
    markup.add(KeyboardButton('Гранты', callback_data='grant'))
    markup.add(KeyboardButton('Обучение', callback_data='edu'))
    markup.add(KeyboardButton('Мероприятия', callback_data='event'))
    return markup


def create_keyboard_contest():
    button = KeyboardButton('Сегодня', callback_data='today1')
    markup = ReplyKeyboardMarkup(resize_keyboard=True).row(button)
    markup.add(KeyboardButton('В этом месяце', callback_data='month1'))
    markup.add(KeyboardButton('Скоро', callback_data='soon1'))
    markup.add(KeyboardButton('В начало 😎', callback_data='return'))
    return markup


def create_keyboard_grant():
    button = KeyboardButton('Сегодня', callback_data='today2')
    markup = ReplyKeyboardMarkup(resize_keyboard=True).row(button)
    markup.add(KeyboardButton('В этом месяце', callback_data='month2'))
    markup.add(KeyboardButton('Скоро', callback_data='soon2'))
    markup.add(KeyboardButton('В начало 😎', callback_data='return'))
    return markup


def create_keyboard_edu():
    button = KeyboardButton('Сегодня', callback_data='today3')
    markup = ReplyKeyboardMarkup(resize_keyboard=True).row(button)
    markup.add(KeyboardButton('В этом месяце', callback_data='month3'))
    markup.add(KeyboardButton('Скоро', callback_data='soon3'))
    markup.add(KeyboardButton('В начало 😎', callback_data='return'))
    return markup


def create_keyboard_event():
    button = KeyboardButton('Сегодня', callback_data='today4')
    markup = ReplyKeyboardMarkup(resize_keyboard=True).row(button)
    markup.add(KeyboardButton('В этом месяце', callback_data='month4'))
    markup.add(KeyboardButton('Скоро', callback_data='soon4'))
    markup.add(KeyboardButton('В начало 😎', callback_data='return'))
    return markup
