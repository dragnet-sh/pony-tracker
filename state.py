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
    tracker_id = Required(unicode)
    payload = Required(unicode)
    action = Optional(Action)
    status = Optional(Status)
    last_known_error = Optional(unicode)


sql_debug(False)
db.bind('sqlite', 'tracker.sqlite', create_db = True)
db.generate_mapping(create_tables = True)



@db_session
def init_state(process_id, payload, action, status):
	action = Action.get(label = action)
	status = Status.get(label = status)
	
	Tracker(tracker_id = process_id, payload = payload, action = action, status = status)

@db_session
def init_action():
	actions = [EAction.FILE_PARSING, EAction.FILE_TRANSFER]
	
	for action in actions:
		Action(label = action)

@db_session
def init_status():
	labels = [EStatus.INIT, EStatus.PROGRESS, EStatus.COMPLETED, EStatus.ERROR]
	
	for label in labels:
		Status(label = label)


@db_session
def status_update(process_id, action, satus):
	tracker = Tracker.select(lambda t: t.tracker_id).order_by(desc(Tracker.id)).first()
	tracker.action = Action.get(label = action).id
	tracker.status = Status.get(label = status).id


if __name__ == '__main__':
	
	init_action()
	init_status()

	init_state('tracker-001', 'json-payload', EAction.FILE_TRANSFER, EStatus.PROGRESS)

