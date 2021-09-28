"""•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
                                                       GNU GENERAL PUBLIC LICENSE
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                has been licensed under GNU General Public License
                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•"""
from Import import *
from ꜱᴀʏᴏɴᴀʀᴀ import *
import ᴋʟᴀx_ʙᴀꜱᴇ.rules_sql as sql
from ӄʟǟաʀօɮօȶ import dispatcher
from ꜰᴜɴᴄᴘᴏᴅ.chat_status import user_admin
from ꜰᴜɴᴄᴘᴏᴅ.string_handling import markdown_parser


__mod_name__ = "📠 ʀᴜʟᴇꜱ"


def get_rules(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    send_rules(update, chat_id)



def send_rules(update, chat_id, from_pm=False):
    bot = dispatcher.bot
    user = update.effective_user 
    reply_msg = update.message.reply_to_message
    try:
        chat = bot.get_chat(chat_id)
    except BadRequest as excp:
        if excp.message == "Chat not found" and from_pm:
            bot.send_message(
                user.id,
                f"{ALKL}The rules shortcut for this chat hasn't been set properly! Ask admins to "
                "fix this.\nMaybe they forgot the hyphen in ID",
            )
            return
        else:
            raise

    rules = sql.get_rules(chat_id)
    text = f"{ALKL}The rules for *{escape_markdown(chat.title)}* are:\n\n{rules}"

    if from_pm and rules:
        bot.send_message(
            user.id, text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
        )
    elif from_pm:
        bot.send_message(
            user.id,
            f"{ALKL}The group admins haven't set any rules for this chat yet. "
            "This probably doesn't mean it's lawless though...!",
        )
    elif rules and reply_msg:
        reply_msg.reply_text(
            "Please click the button below to see the rules.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Rules", url=f"t.me/{bot.username}?start={chat_id}"
                        )
                    ]
                ]
            ),
        )
    elif rules:
        update.effective_message.reply_text(
            f"{ALKL}Please click the button below to see the rules.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Rules", url=f"t.me/{bot.username}?start={chat_id}"
                        )
                    ]
                ]
            ),
        )
    else:
        update.effective_message.reply_text(
            f"{ALKL}The group admins haven't set any rules for this chat yet. "
            "This probably doesn't mean it's lawless though...!"
        )


@user_admin
def set_rules(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    msg = update.effective_message  # type: Optional[Message]
    raw_text = msg.text
    # use python's maxsplit to separate cmd and args
    args = raw_text.split(None, 1)
    if len(args) == 2:
        txt = args[1]
        # set correct offset relative to command
        offset = len(txt) - len(raw_text)
        markdown_rules = markdown_parser(
            txt, entities=msg.parse_entities(), offset=offset
        )

        sql.set_rules(chat_id, markdown_rules)
        update.effective_message.reply_text(
            f"{ALKL}Successfully set rules for this group.")


@user_admin
def clear_rules(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    sql.set_rules(chat_id, "")
    update.effective_message.reply_text(f"{ALKL}Successfully cleared rules!")


def __stats__():
    return f"{ALKL}• {sql.num_chats()} chats have rules set."


def __import_data__(chat_id, data):
    # set chat rules
    rules = data.get("info", {}).get("rules", "")
    sql.set_rules(chat_id, rules)


def __migrate__(old_chat_id, new_chat_id):
    sql.migrate_chat(old_chat_id, new_chat_id)


def __chat_settings__(chat_id, user_id):
    return f"{ALKL}This chat has had it's rules set: `{bool(sql.get_rules(chat_id))}`"


__help__ = f"""{ALKL}
🦀 •/rules-\n get the rules for this chat.

*Admins only*-\n
🦀 •/setrules <your rules here>-\n set the rules for this chat.
🦀 •/clearrules-\n clear the rules for this chat.
"""


GET_RULES_HANDLER = CommandHandler(
    "rules", get_rules, filters=Filters.chat_type.groups, run_async=True)
SET_RULES_HANDLER = CommandHandler(
    "setrules", set_rules, filters=Filters.chat_type.groups, run_async=True)
RESET_RULES_HANDLER = CommandHandler(
    "clearrules", clear_rules, filters=Filters.chat_type.groups, run_async=True)

dispatcher.add_handler(GET_RULES_HANDLER)
dispatcher.add_handler(SET_RULES_HANDLER)
dispatcher.add_handler(RESET_RULES_HANDLER)
