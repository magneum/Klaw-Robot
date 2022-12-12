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
from Sqlbase import SESSION, BASE
from TMemory import *


class PrivateNotes(BASE):
    __tablename__ = "private_notes"
    chat_id = Column(String(14), primary_key=True)
    setting = Column(Boolean, default=False)

    def __init__(self, chat_id, setting):
        self.chat_id = str(chat_id)  # Ensure String
        self.setting = str(setting)


PrivateNotes.__table__.create(checkfirst=True)


def get_private_notes(chat_id) -> bool:
    try:
        private_notes = SESSION.query(PrivateNotes).get(str(chat_id))
        if private_notes:
            return private_notes.setting
        return False
    finally:
        SESSION.close()


def set_private_notes(chat_id, setting: bool):
    with PRIVATE_NOTES_INSERTION_LOCK:
        private_notes = SESSION.query(PrivateNotes).get(str(chat_id))
        if not private_notes:
            private_notes = PrivateNotes(str(chat_id), setting=setting)

        private_notes.setting = setting
        SESSION.add(private_notes)
        SESSION.commit()


def migrate_chat(old_chat_id, new_chat_id):
    with PRIVATE_NOTES_INSERTION_LOCK:
        chat_filters = (
            SESSION.query(PrivateNotes)
            .filter(PrivateNotes.chat_id == str(old_chat_id))
            .all()
        )
        for filt in chat_filters:
            filt.chat_id = str(new_chat_id)
        SESSION.commit()
