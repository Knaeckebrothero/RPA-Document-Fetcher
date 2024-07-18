"""
This module holds the mail.Client class.
"""
import os
import imaplib
from config.custom_logger import configure_custom_logger


class Client:
    """
    This class is responsible for managing
    """

    def __init__(self, imap_server: str, imap_port: int, username: str,
                 password: str, inbox: str = None):
        """
        Automatically connects to the mailclient, using the provided credentials,
        once the class is instantiated.

        :param imap_server: The imap server to connect to.
        :param imap_port: The port of the imap server.
        :param username: The username/mail to connect to.
        :param password: The user's password.
        :param inbox: Inbox to connect to. Defaults to None.
        """
        # Check environment variables for log level
        if os.getenv('LOG_LEVEL'):
            log_level = int(os.environ['LOG_LEVEL'])
        else:
            log_level = 30

        # Initialize the logger
        self.logger = configure_custom_logger(module_name='main', console_level=log_level, file_level=log_level)
        self.logger.debug('Logger initialized')

        # Set the class attributes
        self._imap_server = imap_server
        self._imap_port = imap_port
        self._username = username
        self._password = password
        self.mail = None
        self.inbox = None
        self.logger.debug('Class attributes set')

        # Connect to the inbox
        self.logger.debug('Connecting to the mail server...')
        self.connect()
        self.logger.debug('Connected!')

    def __del__(self):
        """
        Destructor for the mailbox class.
        Automatically closes the connection to the server when the class is destroyed.
        """
        self.logger.info('Closing the connection to the mail server...')
        self.close()

    def connect(self):
        """
        Method to connect to the mailserver using the classes credentials.
        It connects to the inbox attribute to connect to.
        Defaults to None, which will connect to the default inbox.
        """
        self.mail = imaplib.IMAP4_SSL(host=self._imap_server, port=self._imap_port)
        self.mail.login(user=self._username, password=self._password)

        if self.inbox:
            self.select_inbox()

    def close(self):
        """
        Closes the mailclient and logs out of the server.
        Sets the mail attribute to None.
        """
        self.mail.logout()
        self.mail = None

    def select_inbox(self, inbox: str = None):
        """
        Method to select an inbox.

        Args:
            inbox (): The inbox to select.
        """
        self.mail.select(inbox)
        self.inbox = inbox

    def list_inboxes(self):
        """
        Method to get a list of possible inboxes.
        """
        return self.mail.list()[1]
