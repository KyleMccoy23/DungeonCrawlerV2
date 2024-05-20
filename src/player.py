
# from enemy import Enemy
from entity import Entity


class Player(Entity):

    def __init__(self) -> None:
        super().__init__()
        
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

    def attack(self, target: Entity) -> None:
        target.status['health'] -= self.hand.damage
        target.status['health'] = max(target.status.get('health',0), 0)
        target.healthBar.update()

    def unequip(self):
        self.hand = self.defaultWeapon
    