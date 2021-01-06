from telethon import TelegramClient, events, sync
from decouple import config
import json
from random import choice

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
                self.aliases = self.get_aliases_choices(friend['alias'], friend['name'])
                
                self.client.send_message(friend['id'], self.get_rand_msg_dia(friend['has_affetuos']))
                
                if friend['has_work'] :
                    self.client.send_message(friend['id'], self.get_rand_msg_trabalho())
                    
    def get_rand_msg_dia(self, has_affetuos) -> str:
        possible_messages = [
            'Bom dia',
            'Bundia',
            'Bom dia hoje pra ti'
        ]
        
        if has_affetuos :
            possible_messages.append([
                "bom dia meu lindo",
                "Bom dia fofo"
            ])
            
        return "{} {}".format( choice(possible_messages), choice(self.aliases)  )
        
    def get_rand_msg_trabalho(self) -> str:
        possible_messages = [
            'Bom trabalho pra ti',
            'Tenha um bom trabalho',
            'Bom trabson',
            'Bom trabalho hoje',
        ]

        return choice(possible_messages)
    
    
    def get_aliases_choices(self, alias, name) -> object:
        if alias :
            return [ 
                ""
                "{}".format(choice(alias)),
                "{}!".format(choice(alias))
            ]
        else: 
            return [ 
                ""
                "{}".format(name),
                "{}!".format(name)
            ]
    
