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
from Sqlbase import BASE, SESSION
from TMemory import *


class ClearCmd(BASE):
    __tablename__ = "clear_cmd"
    chat_id = Column(String(14), primary_key=True)
    cmd = Column(UnicodeText, primary_key=True, nullable=False)
    time = Column(Integer)

    def __init__(self, chat_id, cmd, time):
        self.chat_id = chat_id
        self.cmd = cmd
        self.time = time


ClearCmd.__table__.create(checkfirst=True)


def get_allclearcmd(chat_id):
    try:
        return SESSION.query(ClearCmd).filter(ClearCmd.chat_id == str(chat_id)).all()
    finally:
        SESSION.close()


def get_clearcmd(chat_id, cmd):
    try:
        clear_cmd = SESSION.query(ClearCmd).get((str(chat_id), cmd))
        if clear_cmd:
            return clear_cmd
        return False
    finally:
        SESSION.close()


def set_clearcmd(chat_id, cmd, time):
    with CLEAR_CMD_LOCK:
        clear_cmd = SESSION.query(ClearCmd).get((str(chat_id), cmd))
        if not clear_cmd:
            clear_cmd = ClearCmd(str(chat_id), cmd, time)

        clear_cmd.time = time
        SESSION.add(clear_cmd)
        SESSION.commit()


def del_clearcmd(chat_id, cmd):
    with CLEAR_CMD_LOCK:
        del_cmd = SESSION.query(ClearCmd).get((str(chat_id), cmd))
        if del_cmd:
            SESSION.delete(del_cmd)
            SESSION.commit()
            return True
        else:
            SESSION.close()
        return False


def del_allclearcmd(chat_id):
    with CLEAR_CMD_LOCK:
        del_cmd = SESSION.query(ClearCmd).filter(ClearCmd.chat_id == str(chat_id)).all()
        if del_cmd:
            for cmd in del_cmd:
                SESSION.delete(cmd)
                SESSION.commit()
            return True
        else:
            SESSION.close()
        return False


def migrate_chat(old_chat_id, new_chat_id):
    with CLEAR_CMD_LOCK:
        chat_filters = (
            SESSION.query(ClearCmd).filter(ClearCmd.chat_id == str(old_chat_id)).all()
        )
        for filt in chat_filters:
            filt.chat_id = str(new_chat_id)
        SESSION.commit()
