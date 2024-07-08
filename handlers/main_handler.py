from datetime import datetime

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile
from aiogram.fsm.context import FSMContext
from keyboards import static_kb, async_kb

from utils import payment, google_sheets, utils

from states.google_sheet import GoogleSheets

router = Router()


# Обработчик команды /start
@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Здравствуйте {message.from_user.first_name}, выберите действие.',
                         reply_markup=static_kb.main_keyboard)


# Обработчик кнопки с ссылкой на яндекс карты
@router.message(F.text == 'Кнопка 1(Yandex)')
async def get_map(message: Message):
    await message.answer('Какой-то текст и ссылка на карту...', reply_markup=static_kb.map_button)


# Обработчик кнопки с ссылкой на оплату 2 р
@router.message(F.text == 'Кнопка 2(Оплата)')
async def pay(message: Message):
    # Передаю URL на оплату из функции, которая его создает, в кнопку для оплаты
    try:
        url = await payment.invoice_for_payment()
        await message.answer('Ссылка на оплату сформирована:', reply_markup=await async_kb.payment_button(url))
    except Exception:
        await message.answer('Ошибка')


# Обработчик кнопки с картинкой и текстом
@router.message(F.text == 'Кнопка 3(Картинка)')
async def send_photo(message: Message):
    # Забираю картинку локально с помощью спец. функции для работы с локальными файлами
    photo = FSInputFile('images/img1.png')
    await message.answer_photo(photo, caption='Какой-то текст под картинкой...')


# Обработчик кнопки c подключением к google таблице и взятем значение из ячейки A2
@router.message(F.text == 'Кнопка 4(Гугл табличка)')
async def get_a2_sheet(message: Message):
    # Забираем экземпляр листа из гугл таблицы и получаем значение ячейки A2
    try:
        sheet = await google_sheets.get_sheet()
        note = sheet.get('A2').first()
        await message.answer(note)
    except Exception:
        await message.answer('Ошибка')


# Обработчик кнопки c вводом даты и ее валидация
@router.message(F.text == 'Текст ввода')
async def check_date(message: Message, state: FSMContext):
    # Прошу пользователя ввести дату, в качестве примера валидной даты используется текущая дата в формате
    # день-месяц-год
    today_date = datetime.now().strftime('%d-%m-%Y')
    await message.answer(f'Введите дату(пример: {today_date})')
    await state.set_state(GoogleSheets.insert_date)


# Обработчик кнопки c вводом даты и ее валидация
@router.message(GoogleSheets.insert_date)
async def check_date_2(message: Message):
    # Получаю сообщение отправленное пользователем, благодаря машине состояний - мы обрабатываем сообщение
    # исключительно из предыдущей функции
    user_date = message.text
    # Вызываем функцию, которая проверяет валидность даты: условие валидности - соответствие формату(не стал добавлять
    # валидацию по временным рамкам, например дата только <= текущей даты)
    if await utils.valid_date(user_date):
        # Получаю экземпляр листа табилицы и записываю данные в столбец B если дата прошла валидацию(использую метод
        # обновления ячейки т.к если просто добавлять, то автоматичски значение будет добавлено в ячейку A).
        try:
            sheet = await google_sheets.get_sheet()
            column = 2
            last_row = len(sheet.get_all_values())
            sheet.update_cell(last_row + 1, column, user_date)
            await message.answer('Дата верна')
        except Exception:
            await message.answer('Ошибка')
    else:
        await message.answer('Дата неверна')
