from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","12227067"))
API_HASH = getenv("API_HASH","b463bedd791aa733ae2297e6520302fe")
BOT_TOKEN = getenv("BOT_TOKEN","6615530566:AAE4eTgWaeLomDvGZTETK4dOnZ1rxx7eb60")
OWNER_ID = int(getenv("OWNER_ID", "5360305806"))
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://AMBOT:AMBOT@ambot.uecutzy.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN", "AMBOTYT")
