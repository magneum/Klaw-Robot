"""•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
                                                       GNU GENERAL PUBLIC LICENSE
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                has been licensed under GNU General Public License
                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•"""
import os
import spamwatch
import telegram.ext as tg
from ᴍᴇᴍᴏɪʀᴇ.ᴍᴇᴍᴏɪʀᴇ import *
from logging import INFO, basicConfig, getLogger
from ꜰᴜɴᴄᴘᴏᴅ.handlers import (
    CustomCommandHandler, CustomMessageHandler, CustomRegexHandler)
"""•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
                                                       GNU GENERAL PUBLIC LICENSE
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                has been licensed under GNU General Public License
                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•"""
basicConfig(
    format="%(levelname)s - %(message)s",
    level=INFO)
LOGS = getLogger(__name__)
ENV = bool(os.environ.get("ENV", False))
TOKEN = os.environ.get("TOKEN", None)
JOIN_LOGGER = os.environ.get("JOIN_LOGGER", None)
EVENT_LOGS = os.environ.get("EVENT_LOGS", None)
API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
LOAD = os.environ.get("LOAD", "").split()
NO_LOAD = os.environ.get("NO_LOAD", "").split()
DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
WORKERS = int(os.environ.get("WORKERS", 8))
BAN_STICKER = os.environ.get(
    "BAN_STICKER", "CAADAgADOwADPPEcAXkko5EB3YGYAg")
SPAMWATCH_SUPPORT_CHAT = os.environ.get("SPAMWATCH_SUPPORT_CHAT", None)
SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", None)
LOGGER = True
OWNER_ID = 1836310130
OWNER_USERNAME = "@HypeVoidSoul"
SUPPORT_CHAT = "HypeVoids"
ALLOW_CHATS = True
DEV_USERS = [1836310130]
KLAW_LINGS = []
WEBHOOK = False
INFOPIC = True
URL = None
DEL_CMDS = True
STRICT_GBAN = True
ALLOW_EXCL = True
SPAMMERS = None
BL_CHATS = set(int(x) for x in os.environ.get("BL_CHATS", "").split())
KLAW_LINGS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)
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


tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler
