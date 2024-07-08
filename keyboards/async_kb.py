from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Динамическая кнопка для оплаты, т.к URL не статический, а генерируется
async def payment_button(url):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Оплатить', url=url))
    return keyboard.adjust(1).as_markup()