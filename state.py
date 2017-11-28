'''The State Tracker'''
__author__ = 'bbudhathoki'

from enum import Enum
from pony.orm import *

'''
Status | Action - ENUM Definition
'''

class EStatus(Enum):
    INIT = 'Initializing'
    PROGRESS = 'In Progress'
    COMPLETED = 'Completed'
    ERROR = 'Error'


class EAction(Enum):
    FILE_PARSING = 'File Parser'
    FILE_TRANSFER = 'FTP Transfer'


'''
Pony ORM - The tracker, tracks the progress on where the sent file is !!
The Status holds the various status label along with its unique code !!

Ref: https://docs.ponyorm.com/queries.html
'''

db = Database()


class Action(db.Entity):
    label = Required(unicode)
    tracker = Set('Tracker')

class Status(db.Entity):
    label = Required(unicode)
    tracker = Set('Tracker')

class Tracker(db.Entity):
    udh_id = Required(unicode)
    udh_payload = Required(unicode)
    action = Optional(Action)
    status = Optional(Status)
    last_known_error = Optional(unicode)


sql_debug(False)
db.bind('sqlite', 'tracker.sqlite', create_db=True)
db.generate_mapping(create_tables=True)

