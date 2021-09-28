"""•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
                                                       GNU GENERAL PUBLIC LICENSE
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                has been licensed under GNU General Public License
                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•"""
from ꜰᴜɴᴄᴘᴏᴅ.handlers import (
    CustomCommandHandler, CustomMessageHandler, CustomRegexHandler)
from Import import *
from logging import INFO, basicConfig, getLogger
from ᴍᴇᴍᴏɪʀᴇ.ᴍᴇᴍᴏɪʀᴇ import *
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
TOKEN = os.environ.get("TOKEN")
OWNER_ID = int(os.environ.get("OWNER_ID"))
JOIN_LOGGER = os.environ.get("JOIN_LOGGER")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
KLAW_LINGS = set(int(x) for x in os.environ.get("KLAW_LINGS" or []))
DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS" or []))
EVENT_LOGS = os.environ.get("EVENT_LOGS")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
LOAD = os.environ.get("LOAD")
NO_LOAD = os.environ.get("NO_LOAD")
DEL_CMDS = os.environ.get("DEL_CMDS")
STRICT_GBAN = os.environ.get("STRICT_GBAN")
WORKERS = os.environ.get("WORKERS")
BAN_STICKER = os.environ.get("BAN_STICKER")
ALLOW_EXCL = os.environ.get("ALLOW_EXCL")
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT")
SPAMWATCH_SUPPORT_CHAT = os.environ.get("SPAMWATCH_SUPPORT_CHAT")
SPAMWATCH_API = os.environ.get("SPAMWATCH_API")
INFOPIC = ӄʟǟաʀօɮօȶ_IMG
BL_CHATS = set(int(x) for x in os.environ.get("BL_CHATS" or []))
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
