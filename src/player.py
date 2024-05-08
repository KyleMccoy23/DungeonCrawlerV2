
from entity import Entity


class Player(Entity):
    """
    Represents a player character in the game world.

    This class inherits from the Entity class and extends its functionality to represent player-specific attributes and behavior.

    Attributes:
        Inherits all attributes from the Entity class:
            defaultWeapon: The default weapon of the player.
            hand: The currently equipped weapon in the player's hand.
            info: A dictionary containing information about the player, such as name, class, race, and status.
            stats: A dictionary containing the statistics of the player, such as Strength, Dexterity, etc.
            inventory: A dictionary mapping Item instances to their quantities in the player's inventory.

    Methods:
        Inherits all methods from the Entity class:
            __init__: Initializes the player with default values.
            __str__: Returns a string representation of the player.
            getInfo(info: str) -> str: Retrieves specific information about the player.
            getItem(itemName: str) -> int: Retrieves the quantity of a specific item in the player's inventory.
            getStat(stat: str) -> int: Retrieves the value of a specific statistic for the player.
    """
    def __init__(self) -> None:
        super().__init__()
    
        self.healthBar = None
        self.manaBar = None
        self.staminaBar = None

        self.bars = []

    def __str__(self) -> str:
        return super().__str__() + f"\nStats:\n{self.stats}"

    def setBars(self, bars:list) -> None:
        self.bars = bars
        self.healthBar = bars[0]
        self.manaBar = bars[1]
        self.staminaBar = bars[2]
    
    def setStatus(self, status:str, value:int) -> None:
        self.status[status] = value

    def setInfo(self, info:str, value:str) -> None:
        self.info[info] = value
    
    def setStat(self, stat:str, value:int) -> None:
        self.stats[stat] = value