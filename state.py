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


