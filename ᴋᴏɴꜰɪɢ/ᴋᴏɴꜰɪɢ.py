import os
class ӄօռʟӼ(object):
    TOKEN = os.environ.get("TOKEN", None)
    JOIN_LOGGER = os.environ.get("JOIN_LOGGER", None)
    KLAW_LINGS = set(int(x) for x in os.environ.get("KLAW_LINGS", "").split())
    DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
    EVENT_LOGS = os.environ.get("EVENT_LOGS", None)
    API_ID = os.environ.get("API_ID", None)
    API_HASH = os.environ.get("API_HASH", None)
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "").split()
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
    WORKERS = int(os.environ.get("WORKERS", 8))
    BAN_STICKER = os.environ.get("BAN_STICKER", "CAADAgADOwADPPEcAXkko5EB3YGYAg")
    SPAMWATCH_SUPPORT_CHAT = os.environ.get("SPAMWATCH_SUPPORT_CHAT", None)
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    SQLALCHEMY_DATABASE_URI =os.environ.get("SQLALCHEMY_DATABASE_URI", None)
    LOGGER = True
    OWNER_ID = 123456789  
    OWNER_USERNAME = "@HypeVoidSoul"
    SUPPORT_CHAT = "HypeVoids"  
    ALLOW_CHATS = True
    DEV_USERS = [123456789]
    KLAW_LINGS = [123456789]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    DEL_CMDS = True  
    STRICT_GBAN = True
    ALLOW_EXCL = True  
    SPAMMERS = None
class Faigo(ӄօռʟӼ):
    LOGGER = True