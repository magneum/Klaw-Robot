"""•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
                                                       GNU GENERAL PUBLIC LICENSE
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                has been licensed under GNU General Public License
                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•"""
from ӄʟǟաʀօɮօȶ import dispatcher, LOGS
from ꜰᴜɴᴄᴘᴏᴅ.chat_status import user_admin, can_delete
from Import import *
from ꜱᴀʏᴏɴᴀʀᴀ import *
from ᴍᴇᴍᴏɪʀᴇ import *

__mod_name__ = "🧴 ᴘᴜʀɢᴇ"

run_async


@user_admin
def purge(update: Update, context: CallbackContext):
    args = context.args
    msg = update.effective_message
    if msg.reply_to_message:
        user = update.effective_user
        chat = update.effective_chat
        if can_delete(chat, context.bot.id):
            message_id = msg.reply_to_message.message_id
            delete_to = msg.message_id - 1
            if args and args[0].isdigit():
                new_del = message_id + int(args[0])
                if new_del < delete_to:
                    delete_to = new_del

            for m_id in range(delete_to, message_id - 1, -1):
                try:
                    context.bot.deleteMessage(chat.id, m_id)
                except BadRequest as err:
                    if err.message == "Message can't be deleted":
                        context.bot.send_message(chat.id, f"{ALKL}\n\nCannot delete all messages. The messages may be too old, I might "
                                                 "not have delete rights, or this might not be a supergroup.")

                    elif err.message != "Message to delete not found":
                        LOGS.exception("Error while cleaning chat messages.")

            try:
                msg.delete()
            except BadRequest as err:
                if err.message == "Message can't be deleted":
                    context.bot.send_message(chat.id, f"{ALKL}\n\nCannot delete all messages. The messages may be too old, I might "
                                             "not have delete rights, or this might not be a supergroup.")

                elif err.message != "Message to delete not found":
                    LOGS.exception("Error while cleaning chat messages.")

            context.bot.send_message(chat.id, f"{ALKL}\n\nCleaning Done.")

            return "<b>{}:</b>" \
                   "\n#PURGE" \
                   "\n<b>Admin:</b> {}" \
                   "\nPurged <code>{}</code> messages.".format(html.escape(chat.title),
                                                               mention_html(
                                                                   user.id, user.first_name),
                                                               delete_to - message_id)

    else:
        msg.reply_photo(
            ӄʟǟաʀօɮօȶ_IMG, f"{ALKL}\n\nReply to a message to select where to start cleaning from.")

    return ""


PURGE_HANDLER = CommandHandler(
    "purge", purge, filters=Filters.chat_type.groups, pass_args=True)
dispatcher.add_handler(PURGE_HANDLER)
