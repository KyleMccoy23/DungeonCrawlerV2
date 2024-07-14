
# from enemy import Enemy
from .entity import Entity


class Player(Entity):

    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return super().__str__() + f"\nStats:\n{self.stats}"

    def setBars(self, bars:list) -> None:
        self.healthBar = bars[0]
        self.manaBar = bars[1]
        self.staminaBar = bars[2]

    def unequip(self):
        self.hand = self.defaultWeapon
