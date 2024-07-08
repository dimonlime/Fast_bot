from aiogram.fsm.state import StatesGroup, State


# Список состояний
class GoogleSheets(StatesGroup):
    insert_date = State()
