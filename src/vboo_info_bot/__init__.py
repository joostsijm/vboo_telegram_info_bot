"""Initialize VBOO Info Bot"""

import os
import logging

from dotenv import load_dotenv
import telegram
from telegram.ext import Updater
from rival_regions_wrapper import LocalAuthentication, ApiWrapper


load_dotenv()

# get logger
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
TELEGRAM_LOGGER = logging.getLogger('telegram')
TELEGRAM_LOGGER.setLevel(logging.INFO)

# create file handler
FILE_HANDLER = logging.FileHandler('output.log')
FILE_HANDLER.setLevel(logging.INFO)

# create console handler
STREAM_HANDLER = logging.StreamHandler()
STREAM_HANDLER.setLevel(logging.INFO)

# create formatter and add it to the handlers
FORMATTER = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
STREAM_HANDLER.setFormatter(FORMATTER)
FILE_HANDLER.setFormatter(FORMATTER)

# add the handlers to logger
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(FILE_HANDLER)
TELEGRAM_LOGGER.addHandler(STREAM_HANDLER)
TELEGRAM_LOGGER.addHandler(FILE_HANDLER)

TELEGRAM_KEY = os.environ['TELEGRAM_KEY']
TELEGRAM_BOT = telegram.Bot(token=TELEGRAM_KEY)
TELEGRAM_UPDATER = Updater(TELEGRAM_KEY, use_context=True)


class MissingAuthenticationError(Exception):
    """Error for missing authentication"""

RR_USERNAME = os.environ.get('RIVAL_REGIONS_USERNAME', None)
RR_PASSWORD = os.environ.get('RIVAL_REGIONS_PASSWORD', None)
RR_LOGIN_METHOD = os.environ.get('RIVAL_REGIONS_LOGIN_METHOD', None)

if None in (RR_USERNAME, RR_PASSWORD, RR_LOGIN_METHOD):
    raise MissingAuthenticationError(
        'Load the following variables in your user environment: '
        'RIVAL_REGIONS_USERNAME, RIVAL_REGIONS_PASSWORD, RIVAL_REGIONS_LOGIN_METHOD'
    )

AUTHENTICATION = LocalAuthentication(RR_USERNAME, RR_PASSWORD, RR_LOGIN_METHOD)
API_WRAPPER = ApiWrapper(AUTHENTICATION)
