from .base import *
import sys
import os


# SECRET_KEY is read from environment variable for security
SECRET_KEY = os.getenv('SECRET_KEY')

if (SECRET_KEY is None):
    print('You must set the SECRET_KEY environment variable to a long string')
    sys.exit()

# Debug must be off in production, ignore the environment variable
DEBUG = False

ALLOWED_HOSTS = [
    'donations.triplecrownforheart.ca',
    'fundraising.triplecrownforheart.ca',
    'localhost'
    ]

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

if (EMAIL_HOST_PASSWORD is None):
    print('You must set the EMAIL_HOST_PASSWORD environment variable')
    sys.exit()

# Make links sent be HTTPS
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# Paypal configuration
# To switch to the sandbox account, set PAYPAL_TEST = True
# and set PAYPAL_ACCOUNT to 'stephen-facilitator@triplecrownforheart.com'

PAYPAL_TEST = read_boolean(os.getenv('PAYPAL_TEST'))
PAYPAL_ACCOUNT = os.getenv('PAYPAL_ACCOUNT')
