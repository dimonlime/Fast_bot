from aiogram.fsm.state import StatesGroup, State


# ������ ���������
class GoogleSheets(StatesGroup):
    insert_date = State()
