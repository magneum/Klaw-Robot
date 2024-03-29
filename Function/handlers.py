# •=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
#                                                        GNU GENERAL PUBLIC LICENSE
#                                                          Version 3, 29 June 2007
#                                                 Copyright (C) 2007 Free Software Foundation
#                                             Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
#                                                 of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
#                                                 has been licensed under GNU General Public License
#                                                 𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
# •=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
from Import import *
import Sqlbase.blacklistusers_sql as sql
from ӄʟǟաʀօɮօȶ import ALLOW_EXCL
from ӄʟǟաʀօɮօȶ import DEV_USERS, KLAW_LINGS

if ALLOW_EXCL:
    CMD_STARTERS = ("/", "!")
else:
    CMD_STARTERS = ("/",)


class AntiSpam:
    def __init__(self):
        self.whitelist = (DEV_USERS or []) + (KLAW_LINGS or [])
        Duration.CUSTOM = 15  # Custom duration, 15 seconds
        self.sec_limit = RequestRate(6, Duration.CUSTOM)  # 6 / Per 15 Seconds
        self.min_limit = RequestRate(20, Duration.MINUTE)  # 20 / Per minute
        self.hour_limit = RequestRate(100, Duration.HOUR)  # 100 / Per hour
        self.daily_limit = RequestRate(1000, Duration.DAY)  # 1000 / Per day
        self.limiter = Limiter(
            self.sec_limit,
            self.min_limit,
            self.hour_limit,
            self.daily_limit,
            bucket_class=MemoryListBucket,
        )

    def check_user(self, user):
        """
        Return True if user is to be ignored else False
        """
        if user in self.whitelist:
            return False
        try:
            self.limiter.try_acquire(user)
            return False
        except BucketFullException:
            return True


SpamChecker = AntiSpam()
MessageHandlerChecker = AntiSpam()


class CustomCommandHandler(CommandHandler):
    def __init__(
        self,
        command,
        callback,
        admin_ok=False,
        allow_edit=False,
        run_async=True,
        **kwargs
    ):
        super().__init__(command, callback, **kwargs)

        if allow_edit is False:
            self.filters &= ~(
                Filters.update.edited_message | Filters.update.edited_channel_post
            )

        self.run_async = run_async

    def check_update(self, update):
        if isinstance(update, Update) and update.effective_message:
            message = update.effective_message

            try:
                user_id = update.effective_user.id
            except:
                user_id = None

            if user_id:
                if sql.is_user_blacklisted(user_id):
                    return False

            if message.text and len(message.text) > 1:
                fst_word = message.text.split(None, 1)[0]
                if len(fst_word) > 1 and any(
                    fst_word.startswith(start) for start in CMD_STARTERS
                ):

                    args = message.text.split()[1:]
                    command = fst_word[1:].split("@")
                    command.append(message.bot.username)
                    if user_id == 1087968824:
                        user_id = update.effective_chat.id
                    if not (
                        command[0].lower() in self.command
                        and command[1].lower() == message.bot.username.lower()
                    ):
                        return None
                    if SpamChecker.check_user(user_id):
                        return None
                    filter_result = self.filters(update)
                    if filter_result:
                        return args, filter_result
                    else:
                        return False

    def handle_update(self, update, dispatcher, check_result, context=None):
        run_async = self.run_async
        if context:
            self.collect_additional_context(context, update, dispatcher, check_result)
            if run_async:
                return dispatcher.run_async(
                    self.callback, update, context, update=update
                )
            return self.callback(update, context)

        optional_args = self.collect_optional_args(dispatcher, update, check_result)
        if run_async:
            return dispatcher.run_async(
                self.callback, dispatcher.bot, update, update=update, **optional_args
            )
        return self.callback(dispatcher.bot, update, **optional_args)  # type: ignore

    def collect_additional_context(self, context, update, dispatcher, check_result):
        if isinstance(check_result, bool):
            context.args = update.effective_message.text.split()[1:]
        else:
            context.args = check_result[0]
            if isinstance(check_result[1], dict):
                context.update(check_result[1])


class CustomRegexHandler(MessageHandler):
    def __init__(self, pattern, callback, friendly="", **kwargs):
        super().__init__(Filters.regex(pattern), callback, **kwargs)


class CustomMessageHandler(MessageHandler):
    def __init__(self, filters, callback, friendly="", allow_edit=False, **kwargs):
        super().__init__(filters, callback, **kwargs)
        if allow_edit is False:
            self.filters &= ~(
                Filters.update.edited_message | Filters.update.edited_channel_post
            )

        def check_update(self, update):
            if isinstance(update, Update) and update.effective_message:
                if self.filters(update):
                    if SpamChecker.check_user(user_id):
                        return None
                    return True
                return False
