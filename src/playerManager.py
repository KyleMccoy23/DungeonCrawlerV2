
from error import GameError
from healthBar import healthBar, manaBar, staminaBar
from helperFuncs import clear, bannerLines
from player import Player


class PlayerManager:

    def __init__(self) -> None:
        pass

    
    def newPlayer(self) -> Player:
        clear()
        bannerLines()

        self.player = Player()

        self.player.setInfo('name', input("Enter a Name for you character\n# "))

        self.player.setBars([healthBar(self.player, color='green2'), manaBar(self.player, color="blue2"), staminaBar(self.player, color='green')])
        bannerLines()
        raise GameError('No Player Creation Defined')
    
        return self.player

    def loadPlayer(self) -> Player:
        raise GameError('No Player Loading Defined')
