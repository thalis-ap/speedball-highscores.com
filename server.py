import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

keycode = "sbleaderboarddb"

sheet = client.open(keycode).sheet1  # Open the spreadhseet

def getData():
    return sheet.get_all_records()

def addData(dt):
    return sheet.insert_row(dt, 4)
