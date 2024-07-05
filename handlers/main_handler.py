from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from keyboards import static_kb

from utils import payment

router = Router()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer(f'Здравствуйте {message.from_user.first_name}, выберите действие.', reply_markup=static_kb.main_keyboard)


@router.message(F.text == 'Кнопка 1(Yandex)')
async def check_all_orders(message: Message, state: FSMContext):
    await message.answer('Какой-то текст...', reply_markup=static_kb.button_one)


@router.message(F.text == 'Кнопка 2(Оплата)')
async def check_all_orders(message: Message, state: FSMContext):
    try:
        await payment.get_payment_info()
    except Exception as e:
        print(str(e))