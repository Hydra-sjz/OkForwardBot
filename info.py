from os import environ

API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
CAPTION = environ.get('CAPTION', '<code>{file_name}</code>')
OWNER = int(environ.get('OWNER', '5493832202'))
PRIVATE_BOT = bool(environ.get('PRIVATE_BOT', False))
