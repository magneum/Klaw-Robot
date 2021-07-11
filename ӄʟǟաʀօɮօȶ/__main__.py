from Import import *
from ᴍᴇᴍᴏɪʀᴇ import *
from ӄʟǟաʀօɮօȶ import LOGS, updater
from ᴋʟᴀx import ALL_MODULES

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("ᴋʟᴀx." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__
    if imported_module.__mod_name__.lower() not in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    if hasattr(imported_module, "__help__") and imported_module.__help__:
        HELPABLE[imported_module.__mod_name__.lower()] = imported_module
    if hasattr(imported_module, "__migrate__"):
        MIGRATEABLE.append(imported_module)
    if hasattr(imported_module, "__stats__"):
        STATS.append(imported_module)
    if hasattr(imported_module, "__gdpr__"):
        GDPR.append(imported_module)
    if hasattr(imported_module, "__user_info__"):
        USER_INFO.append(imported_module)
    if hasattr(imported_module, "__import_data__"):
        DATA_IMPORT.append(imported_module)
    if hasattr(imported_module, "__export_data__"):
        DATA_EXPORT.append(imported_module)
    if hasattr(imported_module, "__chat_settings__"):
        CHAT_SETTINGS[imported_module.__mod_name__.lower()] = imported_module
    if hasattr(imported_module, "__user_settings__"):
        USER_SETTINGS[imported_module.__mod_name__.lower()] = imported_module


LOGS.info("—🔥••÷[  ӄʟǟա🦀ʀօɮօȶ  ]÷••🔥—")
LOGS.info("")
LOGS.info("🔥==================================================🔥")
LOGS.info("🦀 Hell Yea.. ӄʟǟա ʀօɮօȶ IS FUCKING READY.🦀")
updater.start_polling(timeout=15, read_latency=4, drop_pending_updates=True)   
LOGS.info("Successfully loaded modules: \n" + str(ALL_MODULES))
LOGS.info("")
LOGS.info("🔥==================================================🔥")
LOGS.info("—🔥••÷[  ӄʟǟա ʀօɮօȶ  ]÷••🔥—")
updater.idle()
updater.stop()