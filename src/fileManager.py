
from error import GameError
from player import Player

import pickle

class FileManager():

    def __init__(self) -> None:
        
        self.MAINPATH = 'data\\saves'

    def loadPlayer(self, playerName:str = '') -> Player:
        try:
            p= pickle.load(open(f"{self.MAINPATH}\\{playerName}", 'rb'))
            return p
        except:
            raise GameError("no player file found", self.loadPlayer)
    
    def savePlayer(self, player:Player) -> None:
        try:
            pickle.dump(player, open(f'{self.MAINPATH}\\{player.getInfo('name')}', 'wb'))
            return
        except:
            open(f'{self.MAINPATH}\\{player.getInfo('name')}', 'x')
            self.savePlayer(player)
        raise GameError("player saving has failed", self.savePlayer)
