from Import import *
from ꜱᴀʏᴏɴᴀʀᴀ import *
import ᴋʟᴀx_ʙᴀꜱᴇ.clear_cmd_sql as sql
from ӄʟǟաʀօɮօȶ import dispatcher
from ꜰᴜɴᴄᴘᴏᴅ.chat_status import user_admin, connection_status


@user_admin
@connection_status
def clearcmd(update: Update, context: CallbackContext):
    chat = update.effective_chat
    message = update.effective_message
    args = context.args
    msg = ""

    commands = [
    "filters",
    "notes",    
    "purge",
    "welcome",
    ]

    if len(args) == 0:
        commands = sql.get_allclearcmd(chat.id)
        if commands:
            msg += "*Command - Time*\n"
            for cmd in commands:
                msg += f"`{cmd.cmd} - {cmd.time} secs`\n"  
        else:
            msg = f"{ALKL}No deletion time has been set for any command in *{chat.title}*"

    elif len(args) == 1:
        cmd = args[0].lower()
        if cmd == "list":
            msg = f"{ALKL}The commands available are:\n"
            for cmd in commands:
                msg += f"• `{cmd}`\n"
        elif cmd == "restore":
            delcmd = sql.del_allclearcmd(chat.id)
            msg = f"{ALKL}Removed all commands from list"
        else:
            cmd = sql.get_clearcmd(chat.id, cmd)
            if cmd:
                msg = f"{ALKL}`{cmd.cmd}` output is set to be deleted after *{cmd.time}* seconds in *{chat.title}*"
            else:
                if cmd not in commands:
                    msg = f"{ALKL}Invalid command. Check module help for more details"
                else:
                    msg = f"{ALKL}This command output hasn't been set to be deleted in *{chat.title}*"

    elif len(args) == 2:
        cmd = args[0].lower()
        time = args[1]
        if cmd in commands:
            if time == "restore":
                sql.del_clearcmd(chat.id, cmd)
                msg = f"{ALKL}Removed `{cmd}` from list"
            elif (5 <= int(time) <= 300):
                sql.set_clearcmd(chat.id, cmd, time)
                msg = f"{ALKL}`{cmd}` output will be deleted after *{time}* seconds in *{chat.title}*"
            else:
               msg = f"{ALKL}Time must be between 5 and 300 seconds"
        else:
            msg = f"{ALKL}Specify a valid command. Use `/clearcmd list` to see available commands"
                
    else:
        msg = f"{ALKL}I don't understand what are you trying to do. Check module help for more details"

    message.reply_text(
        text = msg,
        parse_mode = ParseMode.MARKDOWN
    )


def __migrate__(old_chat_id, new_chat_id):
    sql.migrate_chat(old_chat_id, new_chat_id)


__help__ = f"""{ALKL}
*Get module configuration:*
• `/clearcmd`: provides all commands that has been set in current group with their deletion time
• `/clearcmd list`: list all available commands for this module
• `/clearcmd <command>`: get the deletion time for a specific `<command>`

*Set module configuration:*
• `/clearcmd <command> <time>`: set a deletion `<time>` for a specific `<command>` in current group. All outputs of that command will be deleted in that group after time value in seconds. Time can be set between 5 and 300 seconds

*Restore module configuration:*
• `/clearcmd restore`: the deletion time set for ALL commands will be removed in current group
• `/clearcmd <command> restore`: the deletion time set for a specific `<command>` will be removed in current group
"""

CLEARCMD_HANDLER = CommandHandler("clearcmd", clearcmd, run_async=True)

dispatcher.add_handler(CLEARCMD_HANDLER)

__element__ = "Clear Commands"
__command_list__ = ["clearcmd"]
__handlers__ = [CLEARCMD_HANDLER]
