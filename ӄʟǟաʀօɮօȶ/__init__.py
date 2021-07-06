from Import import *
from logging import INFO, basicConfig, getLogger
from ᴍᴇᴍᴏɪʀᴇ.ᴍᴇᴍᴏɪʀᴇ import *

basicConfig(
format="%(levelname)s - %(message)s",
level=INFO)
LOGS = getLogger(__name__)
ENV = bool(os.environ.get("ENV", False))
if ENV:
    TOKEN = os.environ.get("TOKEN", None)
    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", None))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")
    JOIN_LOGGER = os.environ.get("JOIN_LOGGER", None)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)
    try:
        KLAW_LINGS = set(int(x) for x in os.environ.get("KLAW_LINGS", "").split())
        DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")
    INFOPIC = bool(os.environ.get("INFOPIC", False))
    EVENT_LOGS = os.environ.get("EVENT_LOGS", None)
    URL = os.environ.get("URL", "")  
    API_ID = os.environ.get("API_ID", None)
    API_HASH = os.environ.get("API_HASH", None)
    DB_URI = os.environ.get("DATABASE_URL")
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
    STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", False))
    WORKERS = int(os.environ.get("WORKERS", 8))
    BAN_STICKER = os.environ.get("BAN_STICKER", "CAADAgADOwADPPEcAXkko5EB3YGYAg")
    ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", None)
    SPAMWATCH_SUPPORT_CHAT = os.environ.get("SPAMWATCH_SUPPORT_CHAT", None)
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    ALLOW_CHATS = os.environ.get("ALLOW_CHATS", True)
    try:
        BL_CHATS = set(int(x) for x in os.environ.get("BL_CHATS", "").split())
    except ValueError:
        raise Exception("Your blacklisted chats list does not contain valid integers.")
else:
    from ᴋᴏɴꜰɪɢ.ᴋᴏɴꜰɪɢ import Faigo as ӄօռʟӼ
    TOKEN = ӄօռʟӼ.TOKEN
    try:
        OWNER_ID = int(ӄօռʟӼ.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")
    JOIN_LOGGER = ӄօռʟӼ.JOIN_LOGGER
    OWNER_USERNAME = ӄօռʟӼ.OWNER_USERNAME
    ALLOW_CHATS = ӄօռʟӼ.ALLOW_CHATS
    try:
        KLAW_LINGS = set(int(x) for x in ӄօռʟӼ.KLAW_LINGS or [])
        DEV_USERS = set(int(x) for x in ӄօռʟӼ.DEV_USERS or [])
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")
    EVENT_LOGS = ӄօռʟӼ.EVENT_LOGS
    API_ID = ӄօռʟӼ.API_ID
    API_HASH = ӄօռʟӼ.API_HASH
    DB_URI = ӄօռʟӼ.SQLALCHEMY_DATABASE_URI
    LOAD = ӄօռʟӼ.LOAD
    NO_LOAD = ӄօռʟӼ.NO_LOAD
    DEL_CMDS = ӄօռʟӼ.DEL_CMDS
    STRICT_GBAN = ӄօռʟӼ.STRICT_GBAN
    WORKERS = ӄօռʟӼ.WORKERS
    BAN_STICKER = ӄօռʟӼ.BAN_STICKER
    ALLOW_EXCL = ӄօռʟӼ.ALLOW_EXCL
    SUPPORT_CHAT = ӄօռʟӼ.SUPPORT_CHAT
    SPAMWATCH_SUPPORT_CHAT = ӄօռʟӼ.SPAMWATCH_SUPPORT_CHAT
    SPAMWATCH_API = ӄօռʟӼ.SPAMWATCH_API
    INFOPIC = ӄʟǟաʀօɮօȶ_IMG
    try:
        BL_CHATS = set(int(x) for x in ӄօռʟӼ.BL_CHATS or [])
    except ValueError:
        raise Exception("Your blacklisted chats list does not contain valid integers.")
KLAW_LINGS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)
if not SPAMWATCH_API:
    sw = None
    LOGS.warning("SpamWatch API key missing! recheck your config.")
else:
    try:
        sw = spamwatch.Client(SPAMWATCH_API)
    except:
        sw = None
        LOGS.warning("Can't connect to SpamWatch!")
KLAW_LINGS = list(KLAW_LINGS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)

updater = tg.Updater(
TOKEN,
workers=WORKERS,
use_context=True)
dispatcher = updater.dispatcher


from ꜰᴜɴᴄᴘᴏᴅ.handlers import (CustomCommandHandler,CustomMessageHandler,CustomRegexHandler)

tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler