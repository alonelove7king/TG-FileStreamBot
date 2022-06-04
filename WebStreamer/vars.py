# This file is a part of TG-FileStreamBot

from os import environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    MULTI_CLIENT = False
    API_ID = int(environ.get("API_ID", "392800"))
    API_HASH = str(environ.get("API_HASH", "f7f4316dac3b4959687b46860b44c265"))
    BOT_TOKEN = str(environ.get("BOT_TOKEN", "2045343811:AAH2YutndTCYokHpkk_rn83CeAivJSMIOa0"))
    SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))  # 1 minte
    WORKERS = int(environ.get("WORKERS", "12"))  # 6 workers = 6 commands at once
    BIN_CHANNEL = int(
        environ.get("BIN_CHANNEL", "-1001614830719")
    )  # you NEED to use a CHANNEL when you're using MULTI_CLIENT
    PORT = int(environ.get("PORT", "443"))
    BIND_ADDRESS = str(environ.get("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    HAS_SSL = environ.get("HAS_SSL", True)
    HAS_SSL = True if str(HAS_SSL).lower() == "true" else False
    NO_PORT = environ.get("NO_PORT", False)
    NO_PORT = True if str(NO_PORT).lower() == "true" else False
    if "DYNO" in environ:
        ON_HEROKU = True
        APP_NAME = str(environ.get("APP_NAME", "d1"))
    else:
        ON_HEROKU = False
    FQDN = (
        str(environ.get("FQDN", "d1.kimo.vip"))
        if not ON_HEROKU or environ.get("FQDN")
        else APP_NAME + ".kimo.vip"
    )
    if ON_HEROKU:
        URL = f"https://{FQDN}/"
    else:
        URL = "http{}://{}{}/".format(
            "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
        )

    UPDATES_CHANNEL = str(environ.get('UPDATES_CHANNEL', "King_network7"))
    OWNER_ID = int(environ.get('OWNER_ID', '864476272'))

    BANNED_CHANNELS = list(set(int(x) for x in str(environ.get("BANNED_CHANNELS", "-1001296894100")).split()))
