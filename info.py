from os import environ
import re

id_pattern = re.compile(r'^.\d+$')

API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
CAPTION = environ.get('CAPTION', '<code>{file_name}</code>')
ADMINS = [int(admins) if id_pattern.search(admins) else admins for admins in environ.get('ADMINS', '5493832202').split()]
PRIVATE_BOT = bool(environ.get('PRIVATE_BOT', False))
