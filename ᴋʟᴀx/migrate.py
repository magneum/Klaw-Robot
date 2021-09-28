from Import import *
from ᴍᴇᴍᴏɪʀᴇ import *
from ӄʟǟաʀօɮօȶ import LOGS, dispatcher


def migrate_chats(update: Update, context: CallbackContext):
    msg = update.effective_message
    if msg.migrate_to_chat_id:
        old_chat = update.effective_chat.id
        new_chat = msg.migrate_to_chat_id
    elif msg.migrate_from_chat_id:
        old_chat = msg.migrate_from_chat_id
        new_chat = update.effective_chat.id
    else:
        return

    LOGS.info("Migrating from %s, to %s", str(old_chat), str(new_chat))
    for mod in MIGRATEABLE:
        mod.__migrate__(old_chat, new_chat)

    LOGS.info("Successfully migrated!")
    raise DispatcherHandlerStop


migrate_handler = MessageHandler(Filters.status_update.migrate, migrate_chats)
dispatcher.add_handler(migrate_handler)
