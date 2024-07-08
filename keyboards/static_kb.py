from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Основная клавиатура(меню бота) выполнено с помощью реплай клавиатуры.
main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Кнопка 1(Yandex)'), KeyboardButton(text='Кнопка 2(Оплата)')],
    [KeyboardButton(text='Кнопка 3(Картинка)'), KeyboardButton(text='Кнопка 4(Гугл табличка)')],
    [KeyboardButton(text='Текст ввода')]
], resize_keyboard=True)

# Статичная кнопка со ссылкой на яндекс карты.
map_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ссылка', url='https://yandex.ru/maps/?text=улица Ленина, 1, Зеленоград, Москва')]
])

