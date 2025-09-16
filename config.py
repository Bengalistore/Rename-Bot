import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "25750007"))
API_HASH = os.environ.get("API_HASH", "9707616e3703ade0dec6d951780f9cca")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "7259440235"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "-1002534798811")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002591125289"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "TechifyBots")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ada3f739fed7efdbe7b08.jpg")
