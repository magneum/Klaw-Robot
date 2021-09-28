# •=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
#                                                        GNU GENERAL PUBLIC LICENSE
#                                                          Version 3, 29 June 2007
#                                                 Copyright (C) 2007 Free Software Foundation
#                                             Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
#                                                 of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
#                                                 has been licensed under GNU General Public License
#                                                 𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
# •=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
from telegram import Message
import os
import subprocess
from telethon.sync import TelegramClient
from telethon import functions, types
from telegram.ext import MessageFilter
from telegram import Message, MessageEntity
import asyncio
from telegram.error import BadRequest
from typing import List, Optional
import json
from logging import INFO, basicConfig, getLogger
import pprint
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest 
from sqlalchemy import func, distinct, Column, String, UnicodeText, Integer
import logging
from time import perf_counter
from functools import wraps
from cachetools import TTLCache
from threading import RLock
from telegram import Chat, ChatMember, ParseMode, Update
from telegram.ext import CallbackContext
from telegram.error import BadRequest
from functools import wraps
from telegram import ChatAction, Update
from telegram.ext import CallbackContext
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, Filters
from pyrate_limiter import (
    BucketFullException,
    Duration,
    RequestRate,
    Limiter,
    MemoryListBucket,
)
from time import sleep
from typing import Dict, List
from telegram import MAX_MESSAGE_LENGTH, Bot, InlineKeyboardButton, ParseMode
from telegram.error import TelegramError
from sqlalchemy import Column, String, UnicodeText
import html
from sqlalchemy import Boolean, Column, UnicodeText
import hashlib
import re
from enum import IntEnum, unique
from telegram import Message
from sqlalchemy import Column, String, UnicodeText, Integer, func, distinct
from sqlalchemy import Integer, String, Boolean, Column, UnicodeText
from sqlalchemy import String, Column, Integer, UnicodeText
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import telegram
import re
import time
from typing import Dict, List
import bleach
import markdown2
import emoji
import regex
from telegram import MessageEntity
from telegram.utils.helpers import escape_markdown
from telegram import (
    ChatPermissions,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode,
    Update,
)
from telethon.tl.types import ChannelParticipantsAdmins
from telegram.error import BadRequest
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from telegram.utils.helpers import escape_markdown, mention_html, mention_markdown
import random
import time
from functools import partial
from contextlib import suppress
from typing import Optional
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ParseMode, Update
from telegram.ext.dispatcher import run_async
from telegram.ext import CallbackContext, Filters, CommandHandler

from telegram import (
    CallbackQuery,
    Chat,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    ParseMode,
    Update,
    User,
)
from telegram.error import BadRequest
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    DispatcherHandlerStop,
    Filters,
    MessageHandler,
    run_async,
)
from telegram.utils.helpers import mention_html
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    ParseMode,
    Update,
    User,
)

from time import sleep
from telegram import TelegramError, Update
from telegram.error import BadRequest, Unauthorized
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from telegram import Update, Bot, ParseMode
from telegram.ext import CommandHandler, CallbackContext, run_async
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async

from typing import Optional

from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
from telegram.utils.helpers import escape_markdown
from telegram import Chat, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import BadRequest, Unauthorized
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)

from telegram.utils.helpers import mention_html
from asyncio import sleep
import ast

from telethon import events

from telegram import (
    MAX_MESSAGE_LENGTH,
    InlineKeyboardMarkup,
    Message,
    ParseMode,
    Update,
    InlineKeyboardButton,
)
from telegram.error import BadRequest
from telegram.utils.helpers import escape_markdown, mention_markdown
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    CallbackQueryHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import run_async


from typing import Optional
from telegram import Bot, Chat, ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, run_async
from telegram.utils.helpers import mention_html
from typing import Optional
import importlib

from telegram import Message, Chat, ParseMode, MessageEntity, Update
from telegram import TelegramError, ChatPermissions
from telegram.error import BadRequest
from telegram.ext import CommandHandler, MessageHandler, CallbackContext, Filters
from telegram.ext.dispatcher import run_async
from telegram.utils.helpers import mention_html
from alphabet_detector import AlphabetDetector
import ast
from datetime import datetime
from functools import wraps
from telegram.ext import CallbackContext
ad = AlphabetDetector()



from datetime import datetime

from telegram import ParseMode, Update
from telegram.error import BadRequest, TelegramError, Unauthorized
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from telegram.utils.helpers import mention_html
from telegram import Update
from telegram.error import BadRequest, RetryAfter, Unauthorized
from telegram.ext import CallbackContext, CommandHandler, Filters
from telegram.ext.dispatcher import run_async
from time import sleep
import csv
import json
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    MessageEntity,
    ParseMode,
    Update,
)
from telegram.error import BadRequest, TelegramError, Unauthorized
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    run_async,
)
from telegram.utils.helpers import mention_html, mention_markdown



import uuid
from io import BytesIO
from typing import Union
from telegram.utils.helpers import escape_markdown
from future.utils import string_types
import requests
import traceback
import sys
import pretty_errors
import io
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext, CommandHandler
pretty_errors.mono()
from telegram import ParseMode, Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    RegexHandler,
)
from html import escape
import telegram
from telegram import ParseMode, InlineKeyboardMarkup, Message, InlineKeyboardButton, Update
from telegram.error import BadRequest
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    MessageHandler,
    DispatcherHandlerStop,
    CallbackQueryHandler,
    run_async,
    Filters,
)
from telegram.utils.helpers import mention_html, escape_markdown
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, Update, Bot
from telegram.error import BadRequest, Unauthorized
from telegram.ext import CommandHandler, CallbackQueryHandler, CallbackContext, run_async
from telegram import ParseMode, Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from typing import Union
from telegram import Update, Bot, ParseMode
from telegram.ext import CommandHandler, CallbackContext, run_async
from telegram import ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, run_async
from telegram.utils.helpers import mention_html
from telegram import ParseMode, ChatPermissions, Update
from telegram.error import BadRequest
from telegram.ext import CommandHandler, MessageHandler, CallbackContext, Filters, run_async
from telegram.utils.helpers import mention_html
import spamwatch
import telegram.ext as tg
from telethon import TelegramClient
StartTime = time.time()
import importlib
from sys import argv
from typing import Optional
from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
    Unauthorized,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram import ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
from telegram.utils.helpers import mention_html
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram import ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
from telegram.utils.helpers import mention_html
from typing import Optional, List
from telegram import Message, Chat, Update, User, ChatPermissions
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from telegram.error import BadRequest
from telegram.utils.helpers import mention_html, escape_markdown
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.utils.helpers import mention_html
from telegram.error import BadRequest
from telegram.ext import CallbackContext, run_async, CallbackQueryHandler
import json, time, os
from sqlalchemy import BigInteger, Boolean, Column, Integer, String, UnicodeText
from telegram import ParseMode, Message, Update
from telegram.error import BadRequest
from telegram.ext import CommandHandler, CallbackContext, run_async
from typing import Union
from sqlalchemy import Column, String, UnicodeText, Boolean, Integer, distinct, func
from sqlalchemy import Column, String, UnicodeText, distinct, func
import threading
from sqlalchemy import Boolean, Column, Integer, String, UnicodeText
from telegram.error import BadRequest, Unauthorized
import ast
from sqlalchemy import Boolean, Column, Integer, String, UnicodeText
from sqlalchemy import Column, String, Boolean
from sqlalchemy import Column, String, distinct, func
from sqlalchemy import Boolean, Column, Integer, String, UnicodeText, distinct, func
from sqlalchemy import Column, String, Boolean, UnicodeText
from typing import Union
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy import Column, String, UnicodeText, distinct, func
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    UnicodeText,
    UniqueConstraint,
    func,
)

from sqlalchemy.dialects import postgresql

from sqlalchemy import func, distinct, Column, String, UnicodeText, Integer

from sqlalchemy import Column, String, UnicodeText

from sqlalchemy import Boolean, Column, UnicodeText

from sqlalchemy import Column, String, UnicodeText, Integer, func, distinct
from sqlalchemy import Integer, String, Boolean, Column, UnicodeText
from sqlalchemy import String, Column, Integer, UnicodeText
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import telegram
from telegram import (
    ChatPermissions,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode,
    Update,
)
from telegram.error import BadRequest
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from telegram.utils.helpers import escape_markdown, mention_html, mention_markdown
import random
import time
from functools import partial
from contextlib import suppress
from typing import Optional
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ParseMode, Update
from telegram.ext.dispatcher import run_async
from telegram.ext import CallbackContext, Filters, CommandHandler

from telegram import (
    CallbackQuery,
    Chat,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    ParseMode,
    Update,
    User,
)
from telegram.error import BadRequest
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    DispatcherHandlerStop,
    Filters,
    MessageHandler,
    run_async,
)
from telegram.utils.helpers import mention_html
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    ParseMode,
    Update,
    User,
)

from time import sleep
from telegram import TelegramError, Update
from telegram.error import BadRequest, Unauthorized
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from telegram import Update, Bot, ParseMode
from telegram.ext import CommandHandler, CallbackContext, run_async
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async

from typing import Optional

from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
from telegram.utils.helpers import escape_markdown
from telegram import Chat, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import BadRequest, Unauthorized
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)

from telegram.utils.helpers import mention_html
from asyncio import sleep
import ast

from telethon import events

from telegram import (
    MAX_MESSAGE_LENGTH,
    InlineKeyboardMarkup,
    Message,
    ParseMode,
    Update,
    InlineKeyboardButton,
)
from telegram.error import BadRequest
from telegram.utils.helpers import escape_markdown, mention_markdown
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    CallbackQueryHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import run_async


from typing import Optional
from telegram import Bot, Chat, ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, run_async
from telegram.utils.helpers import mention_html
from typing import Optional
import importlib

from telegram import Message, Chat, ParseMode, MessageEntity, Update
from telegram import TelegramError, ChatPermissions
from telegram.error import BadRequest
from telegram.ext import CommandHandler, MessageHandler, CallbackContext, Filters
from telegram.ext.dispatcher import run_async
from telegram.utils.helpers import mention_html
from alphabet_detector import AlphabetDetector
import ast
from datetime import datetime
from functools import wraps
from telegram.ext import CallbackContext
ad = AlphabetDetector()



from datetime import datetime

from telegram import ParseMode, Update
from telegram.error import BadRequest, TelegramError, Unauthorized
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from telegram.utils.helpers import mention_html
from telegram import Update
from telegram.error import BadRequest, RetryAfter, Unauthorized
from telegram.ext import CallbackContext, CommandHandler, Filters
from telegram.ext.dispatcher import run_async
from time import sleep
import csv
import json
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    MessageEntity,
    ParseMode,
    Update,
)
from telegram.error import BadRequest, TelegramError, Unauthorized
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    run_async,
)
from telegram.utils.helpers import mention_html, mention_markdown



import uuid
from io import BytesIO
from typing import Union
from telegram.utils.helpers import escape_markdown
from future.utils import string_types
import requests
import traceback
import sys
import pretty_errors
import io
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext, CommandHandler
pretty_errors.mono()
from telegram import ParseMode, Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    RegexHandler,
)
from html import escape
import telegram
from telegram import ParseMode, InlineKeyboardMarkup, Message, InlineKeyboardButton, Update
from telegram.error import BadRequest
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    MessageHandler,
    DispatcherHandlerStop,
    CallbackQueryHandler,
    run_async,
    Filters,
)
from telegram.utils.helpers import mention_html, escape_markdown
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, Update, Bot
from telegram.error import BadRequest, Unauthorized
from telegram.ext import CommandHandler, CallbackQueryHandler, CallbackContext, run_async
from telegram import ParseMode, Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from typing import Union
from telegram import Update, Bot, ParseMode
from telegram.ext import CommandHandler, CallbackContext, run_async
from telegram import ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, run_async
from telegram.utils.helpers import mention_html
from telegram import ParseMode, ChatPermissions, Update
from telegram.error import BadRequest
from telegram.ext import CommandHandler, MessageHandler, CallbackContext, Filters, run_async
from telegram.utils.helpers import mention_html
import spamwatch
import telegram.ext as tg
from telethon import TelegramClient
StartTime = time.time()
import importlib
from sys import argv
from typing import Optional
from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
    Unauthorized,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram import ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
from telegram.utils.helpers import mention_html
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram import ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
from telegram.utils.helpers import mention_html
from typing import Optional, List
from telegram import Message, Chat, Update, User, ChatPermissions
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from telegram.error import BadRequest
from telegram.utils.helpers import mention_html, escape_markdown
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.utils.helpers import mention_html
from telegram.error import BadRequest
from telegram.ext import CallbackContext, run_async, CallbackQueryHandler
import json, time, os
from sqlalchemy import BigInteger, Boolean, Column, Integer, String, UnicodeText
from telegram import ParseMode, Message, Update
from telegram.error import BadRequest
from telegram.ext import CommandHandler, CallbackContext, run_async
from typing import Union
from sqlalchemy import Column, String, UnicodeText, Boolean, Integer, distinct, func
from sqlalchemy import Column, String, UnicodeText, distinct, func
import threading
from sqlalchemy import Boolean, Column, Integer, String, UnicodeText
from telegram.error import BadRequest, Unauthorized
import ast
from sqlalchemy import Boolean, Column, Integer, String, UnicodeText
from sqlalchemy import Column, String, Boolean
from sqlalchemy import Column, String, distinct, func
from sqlalchemy import Boolean, Column, Integer, String, UnicodeText, distinct, func
from sqlalchemy import Column, String, Boolean, UnicodeText
from typing import Union
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy import Column, String, UnicodeText, distinct, func
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    UnicodeText,
    UniqueConstraint,
    func,
)

from sqlalchemy.dialects import postgresql

from sqlalchemy import func, distinct, Column, String, UnicodeText, Integer

from sqlalchemy import Column, String, UnicodeText

from sqlalchemy import Boolean, Column, UnicodeText

from sqlalchemy import Column, String, UnicodeText, Integer, func, distinct
from sqlalchemy import Integer, String, Boolean, Column, UnicodeText
from sqlalchemy import String, Column, Integer, UnicodeText
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import telegram
from telegram import (
    ChatPermissions,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode,
    Update,
)
from telegram.error import BadRequest
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from telegram.utils.helpers import escape_markdown, mention_html, mention_markdown
import random
import time
from functools import partial
from contextlib import suppress
from typing import Optional
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ParseMode, Update
from telegram.ext.dispatcher import run_async
from telegram.ext import CallbackContext, Filters, CommandHandler

from telegram import (
    CallbackQuery,
    Chat,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    ParseMode,
    Update,
    User,
)
from telegram.error import BadRequest
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    DispatcherHandlerStop,
    Filters,
    MessageHandler,
    run_async,
)
from telegram.utils.helpers import mention_html
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    ParseMode,
    Update,
    User,
)

from time import sleep
from telegram import TelegramError, Update
from telegram.error import BadRequest, Unauthorized
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from telegram import Update, Bot, ParseMode
from telegram.ext import CommandHandler, CallbackContext, run_async
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async

from typing import Optional

from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
from telegram.utils.helpers import escape_markdown
from telegram import Chat, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import BadRequest, Unauthorized
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)

from telegram.utils.helpers import mention_html
from asyncio import sleep
import ast

from telethon import events

from telegram import (
    MAX_MESSAGE_LENGTH,
    InlineKeyboardMarkup,
    Message,
    ParseMode,
    Update,
    InlineKeyboardButton,
)
from telegram.error import BadRequest
from telegram.utils.helpers import escape_markdown, mention_markdown
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    CallbackQueryHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import run_async


from typing import Optional
from telegram import Bot, Chat, ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, run_async
from telegram.utils.helpers import mention_html
from typing import Optional
import importlib

from telegram import Message, Chat, ParseMode, MessageEntity, Update
from telegram import TelegramError, ChatPermissions
from telegram.error import BadRequest
from telegram.ext import CommandHandler, MessageHandler, CallbackContext, Filters
from telegram.ext.dispatcher import run_async
from telegram.utils.helpers import mention_html
from alphabet_detector import AlphabetDetector
import ast
from datetime import datetime
from functools import wraps
from telegram.ext import CallbackContext
ad = AlphabetDetector()



from datetime import datetime

from telegram import ParseMode, Update
from telegram.error import BadRequest, TelegramError, Unauthorized
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from telegram.utils.helpers import mention_html
from telegram import Update
from telegram.error import BadRequest, RetryAfter, Unauthorized
from telegram.ext import CallbackContext, CommandHandler, Filters
from telegram.ext.dispatcher import run_async
from time import sleep
import csv
import json
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    MessageEntity,
    ParseMode,
    Update,
)
from telegram.error import BadRequest, TelegramError, Unauthorized
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    run_async,
)
from telegram.utils.helpers import mention_html, mention_markdown



import uuid
from io import BytesIO
from typing import Union
from telegram.utils.helpers import escape_markdown
from future.utils import string_types


import requests
import traceback
import sys
import pretty_errors
import io
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext, CommandHandler
pretty_errors.mono()
from telegram import ParseMode, Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    RegexHandler,
)
from html import escape
import telegram
from telegram import ParseMode, InlineKeyboardMarkup, Message, InlineKeyboardButton, Update
from telegram.error import BadRequest
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    MessageHandler,
    DispatcherHandlerStop,
    CallbackQueryHandler,
    run_async,
    Filters,
)
from telegram.utils.helpers import mention_html, escape_markdown
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, Update, Bot
from telegram.error import BadRequest, Unauthorized
from telegram.ext import CommandHandler, CallbackQueryHandler, CallbackContext, run_async
from telegram import ParseMode, Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from typing import Union
from telegram import Update, Bot, ParseMode
from telegram.ext import CommandHandler, CallbackContext, run_async
from telegram import ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, run_async
from telegram.utils.helpers import mention_html
from telegram import ParseMode, ChatPermissions, Update
from telegram.error import BadRequest
from telegram.ext import CommandHandler, MessageHandler, CallbackContext, Filters, run_async
from telegram.utils.helpers import mention_html
import spamwatch
import telegram.ext as tg
from telethon import TelegramClient
StartTime = time.time()
import importlib
from sys import argv
from typing import Optional
from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
    Unauthorized,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram import ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
from telegram.utils.helpers import mention_html
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram import ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
from telegram.utils.helpers import mention_html
from typing import Optional, List
from telegram import Message, Chat, Update, User, ChatPermissions
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from telegram.error import BadRequest
from telegram.utils.helpers import mention_html, escape_markdown
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.utils.helpers import mention_html
from telegram.error import BadRequest
from telegram.ext import CallbackContext, run_async, CallbackQueryHandler
import json, time, os
from sqlalchemy import BigInteger, Boolean, Column, Integer, String, UnicodeText
from telegram import ParseMode, Message, Update
from telegram.error import BadRequest
from telegram.ext import CommandHandler, CallbackContext, run_async
from typing import Union
from sqlalchemy import Column, String, UnicodeText, Boolean, Integer, distinct, func
from sqlalchemy import Column, String, UnicodeText, distinct, func
import threading
from sqlalchemy import Boolean, Column, Integer, String, UnicodeText
from telegram.error import BadRequest, Unauthorized
import ast
from sqlalchemy import Boolean, Column, Integer, String, UnicodeText
from sqlalchemy import Column, String, Boolean
from sqlalchemy import Column, String, distinct, func
from sqlalchemy import Boolean, Column, Integer, String, UnicodeText, distinct, func
from sqlalchemy import Column, String, Boolean, UnicodeText
from typing import Union
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy import Column, String, UnicodeText, distinct, func
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    UnicodeText,
    UniqueConstraint,
    func,
)

from sqlalchemy.dialects import postgresql