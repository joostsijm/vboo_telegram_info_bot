"""Test configuration"""

import os

from rival_regions_wrapper import LocalAuthentication, ApiWrapper
from dotenv import load_dotenv
import pytest
import telegram


load_dotenv()

class MissingEnvironmentError(Exception):
    """Error for missing environment variable"""

@pytest.fixture(scope="module")
def telegram_channel():
    """Set up telegram channel"""
    return os.environ.get('TELEGRAM_CHANNEL', None)

@pytest.fixture(scope="module")
def telegram_bot():
    """Set up telegram bot before test"""
    telegram_key = os.environ.get('TELEGRAM_KEY', None)
    if None in (telegram_key, telegram_channel):
        raise MissingEnvironmentError(
            'Load the following variables in your user environment: '
            'TELEGRAM_KEY'
        )
    return telegram.Bot(token=telegram_key)


@pytest.fixture(scope="module")
def api_wrapper():
    """Set up wrapper before test"""
    rr_username = os.environ.get('RIVAL_REGIONS_USERNAME', None)
    rr_password = os.environ.get('RIVAL_REGIONS_PASSWORD', None)
    rr_login_method = os.environ.get('RIVAL_REGIONS_LOGIN_METHOD', None)
    if None in (rr_username, rr_password, rr_login_method):
        raise MissingEnvironmentError(
            'Load the following variables in your user environment: '
            'RIVAL_REGIONS_USERNAME, RIVAL_REGIONS_PASSWORD, RIVAL_REGIONS_LOGIN_METHOD'
        )
    authentication = LocalAuthentication(rr_username, rr_password, rr_login_method)
    return ApiWrapper(authentication)

def pytest_addoption(parser):
    """Pytest parser options"""
    parser.addoption('--message', action='store_true', dest="message", \
        default=False, help="enable messagedecorated tests")

def pytest_configure(config):
    """Pytest config"""
    if not config.option.message:
        setattr(config.option, 'markexpr', 'not message')
    config.addinivalue_line(
        "markers", "message: send telegram message"
    )
