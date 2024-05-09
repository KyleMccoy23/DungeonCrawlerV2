
from entity import Entity


class Player(Entity):

    def __init__(self) -> None:
        super().__init__()
    
        self.healthBar = None
        self.manaBar = None
        self.staminaBar = None
        
    def __str__(self) -> str:
        return super().__str__() + f"\nStats:\n{self.stats}"

    def setBars(self, bars:list) -> None:
        self.healthBar = bars[0]
        self.manaBar = bars[1]
        self.staminaBar = bars[2]
    
    def setStatus(self, status:str, value:int) -> None:
        self.status[status] = value

    def setInfo(self, info:str, value:str) -> None:
        self.info[info] = value
    
    def setStat(self, stat:str, value:int) -> None:
        self.stats[stat] = value

    def attack(self, target: Entity) -> int:
        target.info['health'] -= self.hand.damage
        target.info['health'] = max(target.info.get('health'), 0)
        target.healthBar.update()

    def unequip(self):
        self.hand = self.defaultWeapon
    