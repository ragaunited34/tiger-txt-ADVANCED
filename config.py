import os

API_ID = API_ID = 29409780

API_HASH = os.environ.get("API_HASH", "be45067a2e30b4c200b2eb1985bf63a5")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7117480496:AAEaFPnQ4dpvvsCLxxlGf52RVDxbSVRsm6Y")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6254332429))

LOG = -1002072661214

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


