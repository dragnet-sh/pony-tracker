'''Push - Pull File form the given remote FTP Lacation'''
__author__ = 'bbudhathoki'

from ftplib import FTP
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

class FtpTransfer:

    ftp = None
    ftp_user = None
    ftp_pass = None

    '''Initialize Connection'''
    def __init__(self, ftp_host, ftp_user, ftp_pass):
        self.ftp_host = ftp_host
        self.ftp_user = ftp_user
        self.ftp_pass = ftp_pass


    '''Connect to the FTP Host'''
    def connect(self):
        try:
            self.ftp = FTP(self.ftp_host)
            self.ftp.login(self.ftp_user, self.ftp_pass)
        except Exception:
            print 'Unable to Connect the the FTP !!'
            return None

    '''Push the given file to Remote'''
    def pull(self, LOCAL_FILE_PATH, remote_file_path):
        localfile = open(LOCAL_FILE_PATH, 'wb')
        self.ftp.retrbinary('RETR ' + remote_file_path, localfile.write, 1024)
        localfile.close()

