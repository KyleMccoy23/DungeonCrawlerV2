


from error import GameError
from healthBar import healthBar, manaBar, staminaBar


class PlayerManager:

    def __init__(self) -> None:
        pass

    
    def newPlayer(self):
        self.player.setBars(healthBar(self.player, color='green2'), manaBar(self.player, color="blue2"), staminaBar(self.player, color='green'))
        raise GameError('No Player Creation Defined')

    
    def loadPlayer(self):
        raise GameError('No Player Loading Defined')