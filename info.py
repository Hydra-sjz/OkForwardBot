from os import environ
import re

id_pattern = re.compile(r'^.\d+$')

API_ID = int(environ.get('API_ID', '13570748'))
API_HASH = environ.get('API_HASH', '5e7dcf76a539a41177fb5b44f767d069')
BOT_TOKEN = environ.get('BOT_TOKEN', '5899045489:AAG8XtuFD1rbkS0dlnFLOzk9molalCAM1C8')
CAPTION = environ.get('CAPTION', '<code>{file_name}</code>')
ADMINS = [int(admins) if id_pattern.search(admins) else admins for admins in environ.get('ADMINS', '5493832202').split()]
PRIVATE_BOT = bool(environ.get('PRIVATE_BOT', False))
