from datetime import datetime


# Отдельная функция для валидации дат
async def valid_date(user_date):
    try:
        datetime.strptime(user_date, '%d-%m-%Y')
        return True
    except ValueError:
        return False
