import os

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'public/static')]
STATIC_URL = '/static/'

GITHUB_CLIENT_ID = os.environ.get('KOBIN_EXAMPLE_GITHUB_CLIENT_ID')
GITHUB_CLIENT_SECRET = os.environ.get('KOBIN_EXAMPLE_GITHUB_CLIENT_SECRET')
