from telethon import TelegramClient, events, sync
from decouple import config
import json

class Automessager(object): 

    def __init__(self):
        super().__init__()
        self.filename     = config('CONTACTS')
        self.session_name = config('APP_NAME')
        self.api_id       = config('API_ID')
        self.api_hash     = config('API_HASH')
        self.client       = TelegramClient(self.session_name, self.api_id , self.api_hash)
        self.client.start()
    
    def start(self):
        with open(self.filename) as json_file:
            data = json.load(json_file)
            for friend in data['friends']:
                self.client.send_message(friend['id'], 'Testando...')
