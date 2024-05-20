from healthBar import healthBar, manaBar, staminaBar
from item import Item, fists

class Entity:
    """
    Represents an entity in the game world.

    Attributes:
        defaultWeapon: The default weapon of the entity.
        hand: The currently equipped weapon in the entity's hand.
        info: A dictionary containing information about the entity, such as name, class, race, and status.
        stats: A dictionary containing the statistics of the entity, such as Strength, Dexterity, etc.
        inventory: A dictionary mapping Item instances to their quantities in the entity's inventory.

    Methods:
        __init__: Initializes the entity with default values.
        __str__: Returns a string representation of the entity.
        getInfo(info: str) -> str: Retrieves specific information about the entity.
        getItem(itemName: str) -> int: Retrieves the quantity of a specific item in the entity's inventory.
        getStat(stat: str) -> int: Retrieves the value of a specific statistic for the entity.  
        getStatus(status: str, value: int) -> None: Sets the value of a specific status for the entity.
    """
    def __init__(self) -> None:

        self.defaultWeapon = fists
        self.hand = self.defaultWeapon

        # self.healthBar = healthBar(self, color='green2')
        # self.manaBar = manaBar(self, color="blue2")
        # self.staminaBar = staminaBar(self, color='green')
        
        self.info:dict[str, str] = {
            'name':'',
            'class':'',
            'race':'',
            'status':'',
        }

        self.status:dict[str, int] = {
            'health':0,
            'mana':0,
            'stamina':0,
            'maxHealth':0,
            'maxMana':0,
            'maxStamina':0,
            'exp':0,
            'level':0,
        }

        self.stats: dict[str, int] = {
            'Str':0,
            'Dex':0,
            'Con':0,
            'Int':0,
            'Wis':0,
            'Cha':0
        }

        self.inventory:dict[Item, int] = {
            fists : 1
        }

    def __str__(self) -> str:
        """
        Returns a string representation of the entity.

        Returns:
            A string containing basic information about the entity and the item currently equipped in its hand.
        """
        return f"Name: {self.getInfo('name')}\nClass: {self.getInfo('class')}\nRace: {self.getInfo('race')}\nHand:{self.hand.name}"

    def getStatus(self, status:str) -> int:
        """
        Gets the value of a specific status for the entity.

        Args:
            status: The name of the status to set (e.g., 'health', 'mana', 'stamina', etc.).

        Returns:
            The value of the specified status for the entity. If the status is not found, returns 0.
        """
        return self.status.get(status, 0)

    def getInfo(self, info:str) -> str:
        """
        Retrieves specific information about the entity.

        Args:
            info: The type of information to retrieve (e.g., 'name', 'class', 'race', 'status').

        Returns:
            The requested information about the entity.
        """
        return self.info.get(info, '')
    
    def getItem(self, itemName) -> int:
        """
        Retrieves the quantity of a specific item in the entity's inventory.

        Args:
            itemName: The name of the item to retrieve.

        Returns:
            The quantity of the specified item in the entity's inventory. If item is not found, returns 0.
        """
        for i in self.inventory:
            if i.name == itemName:
                return self.inventory.get(i, 0)
        return 0
    
    def getStat(self, stat:str) -> int:
        """
        Retrieves the value of a specific statistic for the entity.

        Args:
            stat: The name of the statistic to retrieve (e.g., 'Str', 'Dex', 'Con', etc.).

        Returns:
            The value of the specified statistic for the entity.
        """
        return self.stats.get(stat, 0)
    
