


from error import GameError


class PlayerManager:

    def __init__(self) -> None:
        pass

    
    def newPlayer(self):
        raise GameError('No Player Creation Defined')

    
    def loadPlayer(self):
        raise GameError('No Player Loading Defined')