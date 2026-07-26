from linebot.v3.webhooks import MessageEvent, TextMessageContent
from google_sheet import get_sheet
from config import GOOGLE_SHEET_ID
from datetime import datetime


def handle_text(event):
    sheet = get_sheet(GOOGLE_SHEET_ID)

    now = datetime.now()

    sheet.append_row([
        now.strftime("%Y-%m-%d"),
        now.strftime("%H:%M:%S"),
        event.source.user_id,
        event.message.text
    ])

    print("Saved :", event.message.text)