import os 

class Config(object):
  APP_ID = int(os.environ.get("APP_ID", ""))
  API_HASH = os.environ.get("API_HASH", "")
  TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
  AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
  DOWNLOAD_LOCATION = "./bot/DOWNLOADS"
  DB_URI = os.environ.get("DATABASE_URL", "")
  OWNER_ID = [int(i) for i in os.environ.get("OWNER_ID", "").split(" ")]
  CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION",False)
