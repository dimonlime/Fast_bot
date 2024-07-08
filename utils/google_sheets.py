import gspread
import os
import dotenv
from oauth2client.service_account import ServiceAccountCredentials

# Указываем данные для подключения к Гугл Таблицам
SERVICE_ACCOUNT_FILE = 'configs/credentials.json'
SCOPE = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')


# Функция, которая возвращает экземпляр листа из таблицы
async def get_sheet():
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        SERVICE_ACCOUNT_FILE, SCOPE)
    client = gspread.authorize(creds)
    sheet = client.open_by_url(os.getenv('GOOGLESHEET_URL')).sheet1
    return sheet
