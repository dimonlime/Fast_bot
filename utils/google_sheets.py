import gspread
import os
import dotenv
from oauth2client.service_account import ServiceAccountCredentials

SERVICE_ACCOUNT_FILE = 'configs/credentials.json'
SCOPE = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')


async def get_sheet():
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        SERVICE_ACCOUNT_FILE, SCOPE)
    print(creds)
    client = gspread.authorize(creds)
    print(client.http_client)
    sheet = client.open_by_key(SPREADSHEET_ID).sheet1
    return sheet
