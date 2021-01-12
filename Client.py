import os
import json
from telethon import TelegramClient, events, sync
from decouple import config
from random import choice
from datetime import datetime

class Automessager(object): 

    def __init__(self):
        super().__init__()
        project_folder    = os.path.expanduser(os.path.dirname(os.path.abspath(__file__))) 
        self.filename     = os.path.join(project_folder, config('CONTACTS'))
        self.session_name = config('APP_NAME')
        self.api_id       = config('API_ID')
        self.api_hash     = config('API_HASH')
        self.client       = TelegramClient(self.session_name, self.api_id , self.api_hash)
        self.weeknumber   = datetime.today().weekday()
        self.hours        = datetime.now().hour
        self.client.start()
    
    def start(self):
        with open(self.filename) as json_file:
            data = json.load(json_file)
            for friend in data['friends']:
                self.aliases = self.get_aliases_choices(friend['alias'], friend['name'])
                
                self.client.send_message(friend['id'], self.get_rand_msg_dia(friend['has_affetuos']))
                
                if friend['has_work'] and self.weeknumber < 5 and self.hours < 13:
                    self.client.send_message(friend['id'], self.get_rand_msg_trabalho())
                
                if  self.weeknumber == 5 and self.hours < 13:
                    self.client.send_message(friend['id'], choice([
                        'bom sábado para ti',
                        'e bom sábado também kk',
                        'bom sábado'
                    ]))
            
                if self.weeknumber == 6 and self.hours < 13:
                    self.client.send_message(friend['id'], choice([
                        'bom domingo para ti',
                        'e bom doming também',
                        'bom domingo'
                    ]))
                    
    def get_rand_msg_dia(self, has_affetuos) -> str:
        possible_messages = self.get_saudacoes_type()
    
        if has_affetuos :
            possible_messages = possible_messages + [ 'bom dia meu lindo', 'Bom dia fofo']
        
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
    
    def get_saudacoes_type( self ) -> object:
        if ( self.hours < 12):
            return [
                'Bom dia',
                'Bundia',
                'Bundinha,',
                'Bom dia hoje pra ti'
            ] 
        elif ( self.hours > 18):
            return [
                'Boa noite',
                'Boa noitinha',
            ] 
        else: 
            return ['Boa tarde',
                'Boa tarde, tudo bom',
                'Boa tarde, tudo bem'
            ]
        
