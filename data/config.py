import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
TWO_GIS_MAPS_API_KEY = str(os.getenv("TWO_GIS_MAPS_API_KEY"))
