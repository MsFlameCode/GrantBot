# Указываем путь к JSON
import parser

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

import keyboard
import const

import tg_analytic_linux
import tg_analytic_windows

bot = Bot(token='5442354499:AAEBXSNoEcQAWyGsgUs5puBZwKBmGClIACI')
#bot = Bot(token='5528901938:AAFpZ77W8nsAfLGYphusFio2hjHr4HEpj4A')
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    tg_analytic_linux.statistics(message.from_user.id, message.text)
    await bot.send_message(message.from_user.id, const.CONST_GREETINGS, reply_markup=keyboard.create_keyboard_common())


# @dp.message_handler(commands=['статистика'])
# async def process_help_command(message: types.Message):
#     tg_analytic_linux.statistics(message.chat.id,message.text)
#     st = message.text.split(' ')
#     messages = tg_analytic_linux.analysis(st,message.chat.id)
#     await bot.send_message(message.chat.id, messages)
#     # tg_analytic_linux.statistics( message.from_user.id, message.text)
#     # await bot.send_message(message.from_user.id, const.CONST_HELP)


@dp.message_handler(lambda message: message.text == "В начало 😎")
async def process_start_command(message: types.Message):
    msg = "Выберите интересующую вас категорию"
    await bot.send_message(message.from_user.id, msg, reply_markup=keyboard.create_keyboard_common(),
                           disable_web_page_preview=True)


# обработка кнопки Конкурсы
@dp.message_handler(lambda message: message.text == "Конкурсы")
async def without_puree(message: types.Message):
    tg_analytic_linux.statistics(message.from_user.id, message.text)
    msg = "Выберите период для отображения конкурсов"
    const.CATEGORY = 1
    await bot.send_message(message.from_user.id, msg, reply_markup=keyboard.create_keyboard_grant(),
                           disable_web_page_preview=True)


# обработка кнопки Гранты
@dp.message_handler(lambda message: message.text == "Гранты")
async def without_puree(message: types.Message):
    tg_analytic_linux.statistics(message.from_user.id, message.text)
    msg = "Выберите период для отображения грантов"
    const.CATEGORY = 2
    await bot.send_message(message.from_user.id, msg, reply_markup=keyboard.create_keyboard_grant(),
                           disable_web_page_preview=True)


# обработка кнопки Обучение
@dp.message_handler(lambda message: message.text == "Обучение")
async def without_puree(message: types.Message):
    tg_analytic_linux.statistics(message.from_user.id, message.text)
    msg = "Выберите период для отображения обучений"
    const.CATEGORY = 3
    await bot.send_message(message.from_user.id, msg, reply_markup=keyboard.create_keyboard_edu(),
                           disable_web_page_preview=True)


# обработка кнопки Мероприятия
@dp.message_handler(lambda message: message.text == "Мероприятия")
async def without_puree(message: types.Message):
    tg_analytic_linux.statistics(message.from_user.id, message.text)
    msg = "Выберите период для отображения мероприятий:"
    const.CATEGORY = 4
    await bot.send_message(message.from_user.id, msg, reply_markup=keyboard.create_keyboard_event(),
                           disable_web_page_preview=True)


# получение информации в категории Сегодня
@dp.message_handler(lambda message: message.text == "Сегодня")
async def without_puree(message: types.Message):
    tg_analytic_linux.statistics(message.from_user.id, message.text)
    msg = parser.parse_table_today()
    str = "%s" % (msg)
    await bot.send_message(message.from_user.id, str, reply_markup=keyboard.create_keyboard_contest(),
                           disable_web_page_preview=True)


# получение информации в категории В этом месяце
@dp.message_handler(lambda message: message.text == "В этом месяце")
async def without_puree(message: types.Message):
    tg_analytic_linux.statistics(message.from_user.id, message.text)
    msg = parser.parse_table_month()
    await bot.send_message(message.from_user.id, msg, reply_markup=keyboard.create_keyboard_contest(),
                           parse_mode='Markdown', disable_web_page_preview=True)


# получение информации в категории В этом месяце
@dp.message_handler(lambda message: message.text == "Скоро")
async def without_puree(message: types.Message):
    tg_analytic_linux.statistics(message.from_user.id, message.text)
    msg = parser.parse_table_soon()
    await bot.send_message(message.from_user.id, msg, reply_markup=keyboard.create_keyboard_contest(),
                           parse_mode='Markdown', disable_web_page_preview=True)

@dp.message_handler(content_types=['text'])
async def handle_text(message):
    tg_analytic_linux.statistics(message.chat.id,message.text)
    if message.text[:10] == 'статистика' or message.text[:10] == 'Cтатистика':
        st = message.text.split(' ')
        messages = tg_analytic_linux.analysis(st,message.chat.id)
        await bot.send_message(message.chat.id, messages)

# @dp.message_handler()
# async def echo_message(message: types.Message):
#     msg = "Человек, я не понимаю тебя, нажми нужную кнопку 👇🏻"
#     await bot.send_message(message.from_user.id, msg, reply_markup=keyboard.create_keyboard_grant())

if __name__ == '__main__':
    executor.start_polling(dp)
