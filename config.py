from dotenv import load_dotenv
import os

load_dotenv()

print("CONFIG FILE =", __file__)
print("SECRET =", repr(os.getenv("LINE_CHANNEL_SECRET")))
print("TOKEN =", repr(os.getenv("LINE_CHANNEL_ACCESS_TOKEN")))

LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")