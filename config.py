from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","20457610"))
API_HASH = getenv("API_HASH","b7de0dfecd19375d3f84dbedaeb92537")
BOT_TOKEN = getenv("BOT_TOKEN","7198737383:AAFF_m7PgyD6RK8a31JkB-zEHNYXyIms5ek")
OWNER_ID = int(getenv("OWNER_ID", "6590287973"))
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://vinamratiwari579:m6YDRYH8HbwuEqxt@cluster0.x7ac1wt.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN", "naruto_support1")
