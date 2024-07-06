from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InputFile, InputMediaPhoto
from aiogram.types.input_file import FSInputFile
from aiogram.fsm.context import FSMContext
from keyboards import static_kb

from utils import payment, google_sheets

router = Router()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer(f'Здравствуйте {message.from_user.first_name}, выберите действие.',
                         reply_markup=static_kb.main_keyboard)


@router.message(F.text == 'Кнопка 1(Yandex)')
async def map(message: Message, state: FSMContext):
    await message.answer('Какой-то текст...', reply_markup=static_kb.map_button)


@router.message(F.text == 'Кнопка 2(Оплата)')
async def payment(message: Message, state: FSMContext):
    try:
        await payment.get_payment_info()
    except Exception as e:
        print(str(e))


@router.message(F.text == 'Кнопка 3(Картинка)')
async def send_photo(message: Message, state: FSMContext):
    photo = FSInputFile('images/img1.png')
    await message.answer_photo(photo, caption='text')


@router.message(F.text == 'Кнопка 3(Картинка)')
async def send_photo(message: Message, state: FSMContext):
    photo = FSInputFile('images/img1.png')
    await message.answer_photo(photo, caption='text')


@router.message(F.text == 'Кнопка 4(Гугл табличка)')
async def send_photo(message: Message, state: FSMContext):
    await message.answer('Начинаю взаимодействие с гугл табилцей')
    try:
        name = message.from_user.first_name
        telegram_id = message.from_user.id
        sheet = await google_sheets.get_sheet()
        sheet.append_row([name, telegram_id])
        await message.answer('Успех')
    except Exception as e:
        print(e)



