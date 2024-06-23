
from genericpath import isfile
from ntpath import join
from os import listdir
from error import GameError
import pickle

class FileManager():

    def __init__(self) -> None:
        
        self.MAINPATH = 'data\\saves'

    def loadPlayer(self, playerName:str = ''):
        try:
            p= pickle.load(open(f"{self.MAINPATH}\\{playerName}", 'rb'))
            return p
        except:
            raise GameError("no player file found", self.loadPlayer)
    
    def savePlayer(self, player) -> None:
        try:
            pickle.dump(player, open(f'{self.MAINPATH}\\{player.getInfo('name')}', 'wb'))
            return
        except:
            open(f'{self.MAINPATH}\\{player.getInfo('name')}', 'x')
            self.savePlayer(player)
        raise GameError("player saving has failed", self.savePlayer)

    def getSaveNames(self) -> list:
        return [f for f in listdir(self.MAINPATH) if isfile(join(self.MAINPATH, f))]