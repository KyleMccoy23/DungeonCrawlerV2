
class Item:
    """
    This class represents an item in the game.

    Attributes:
        name (str): The name of the item.
        value (float): The value of the item.
        type (str): The type of the item.
    """

    def __init__(self, 
                 name: str, 
                 value: float, 
                 type: str, 
                 ) -> None:
        """
        Initializes a new instance of the `Item` class.

        Args:
            name (str): The name of the item.
            value (float): The value of the item.
            type (str): The type of the item.
        """
        self.name = name
        self.value = value
        self.type = type
    
    def __str__(self) -> str:
        return f'Name:{self.name}\nType:{self.type}\nValue:{self.value}'

class Weapon(Item):
    def __init__(self,
                 name: str,
                 weaponType: str,
                 damage: int,
                 value: int
                 ) -> None:
        super().__init__(name, 
                         value, 
                         "weapon")
        self.weaponType = weaponType
        self.damage = damage

class SpecialWeapon(Weapon):
    def __init__(self, 
                 name: str, 
                 weaponType: str, 
                 damage: int, 
                 value: int,
                 *attributes) -> None:
        super().__init__(name, 
                         weaponType, 
                         damage, 
                         value)
        self.attributes = attributes

class Potion(Item):
    def __init__(self, name: str, value: float, effect: str, potency: int) -> None:
        super().__init__(name, value, "Potion")
        self.effect = effect
        self.potency = potency


ironSword = Weapon(name="Iron Sword",
                    weaponType="sharp",
                    damage=5,
                    value=10)

shortBow = Weapon(name="Short Bow",
                   weaponType="ranged",
                   damage=4,
                   value=8)

fists = Weapon(name="Fists",
               weaponType="blunt",
               damage=2,
               value=0)

healingPotion = Potion(name='Healing Potion',
                     value=5,
                     effect="healing",
                     potency=1)

excaliber = SpecialWeapon("Excaliber",
                          "Sword",
                          999,
                          9999999,
                          "UBBRAKABLE",
                          "HOLY")

iron = Item(name="Iron",
            value=2,
            type="ingot")

stick = Item(name="stick",
             value=1,
             type='item')
