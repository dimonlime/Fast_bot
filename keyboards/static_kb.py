from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime, timedelta
from aiogram.utils.keyboard import InlineKeyboardBuilder


main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Кнопка 1(Yandex)')],
    [KeyboardButton(text='Кнопка 2(Оплата)')],
    [KeyboardButton(text='Кнопка 3(Картинка)')],
    [KeyboardButton(text='Кнопка 4(Гугл табличка)')],
], resize_keyboard=True)


map_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ссылка', url='https://yandex.ru/maps/?text=улица Ленина, 1, Зеленоград, Москва')]
])