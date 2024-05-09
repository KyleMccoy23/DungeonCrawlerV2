
from error import GameError
from healthBar import healthBar, manaBar, staminaBar
from player import Player


class PlayerManager:

    def __init__(self) -> None:
        pass

    
    def newPlayer(self) -> Player:

        self.player = Player()

        self.player.setBars(healthBar(self.player, color='green2'), manaBar(self.player, color="blue2"), staminaBar(self.player, color='green'))
        raise GameError('No Player Creation Defined')
    
        return self.player

    
    def loadPlayer(self) -> Player:
        raise GameError('No Player Loading Defined')