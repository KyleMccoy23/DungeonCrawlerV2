from healthBar import healthBar, manaBar, staminaBar
from item import Item, fists

class Entity:
    def __init__(self) -> None:
        """
        Initializes a new instance of the Entity class.

        This method initializes the following instance variables:
        - `defaultWeapon`: The default weapon of the entity.
        - `hand`: The currently equipped weapon in the entity's hand.
        - `info`: A dictionary containing information about the entity, such as name, class, race, and status.
        - `status`: A dictionary containing the status of the entity, such as health, mana, stamina, and experience.
        - `stats`: A dictionary containing the statistics of the entity, such as Strength, Dexterity, and Intelligence.
        - `inventory`: A dictionary mapping Item instances to their quantities in the entity's inventory.
        - `healthBar`: A healthBar instance representing the health bar of the entity.
        - `manaBar`: A manaBar instance representing the mana bar of the entity.
        - `staminaBar`: A staminaBar instance representing the stamina bar of the entity.
        - `bars`: A list containing the healthBar, manaBar, and staminaBar instances.

        This method does not take any parameters.

        This method does not return anything.
        """
        self.defaultWeapon = fists
        self.hand = self.defaultWeapon

        self.location:dict = {
            'map':'forest',
            'cords':(0,0)
        }
        
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
            'maxExp':0,
            'level':1,
        }

        self.stats: dict[str, int] = {
            'Str':1,
            'Dex':1,
            'Con':1,
            'Int':1,
            'Wis':1,
            'Cha':1
        }

        self.inventory:dict[Item, int] = {
            fists : 1
        }

        self.healthBar = healthBar(self, color='green2')
        self.manaBar = manaBar(self, color="blue2")
        self.staminaBar = staminaBar(self, color='green')

        self.bars = [self.healthBar, self.manaBar, self.staminaBar]

    def __str__(self) -> str:
        """
        Returns a string representation of the entity.

        Returns:
            A string containing basic information about the entity and the item currently equipped in its hand.
        """
        return f"Name: {self.getInfo('name')}\nClass: {self.getInfo('class')}\nRace: {self.getInfo('race')}\nHand: {self.hand.name}\nHealth: {self.getStatus('health')}/{self.getStatus('maxHealth')}\nMana: {self.getStatus('mana')}/{self.getStatus('maxMana')}\nStamina: {self.getStatus('stamina')}/{self.getStatus('maxStamina')}"

    def getStatus(self, status:str) -> int:
        """
        Returns the value of a specific status for the entity.

        Args:
            status (str): The name of the status to retrieve.

        Returns:
            int: The value of the specified status. If the status is not found, returns 0.
        """
        return self.status.get(status, 0)

    def getInfo(self, info:str) -> str:
        """
        Retrieves specific information about the entity.

        Args:
            info (str): The type of information to retrieve (e.g., 'name', 'class', 'race', 'status').

        Returns:
            str: The requested information about the entity. If the information is not found, returns an empty string.
        """
        return self.info.get(info, '')
    
    def getItem(self, itemName) -> int:
        """
        Retrieves the quantity of a specific item in the entity's inventory.

        Args:
            itemName (str): The name of the item to retrieve.

        Returns:
            int: The quantity of the specified item in the entity's inventory. If item is not found, returns 0.
        """
        for i in self.inventory:
            if i.name == itemName:
                return self.inventory.get(i, 0)
        return 0
    
    def getStat(self, stat:str) -> int:
        """
        Retrieves the value of a specific statistic for the entity.

        Args:
            stat (str): The name of the statistic to retrieve (e.g., 'Str', 'Dex', 'Con', etc.).

        Returns:
            int: The value of the specified statistic for the entity. If the statistic is not found, returns 0.
        """
        return self.stats.get(stat, 0)

    def setStatus(self, status:str, value:int) -> None:
        self.status[status] = value

    def setInfo(self, info:str, value:str) -> None:
        self.info[info] = value
    
    def setStat(self, stat:str, value:int) -> None:
        self.stats[stat] = value

    def attack(self, target) -> None:
        target.status['health'] -= self.hand.damage
        target.status['health'] = max(target.status.get('health',0), 0)
        target.healthBar.update()

    def isDead(self) -> bool:
        """
        Check if the entity is dead by checking if its health status is 0 or less.

        Returns:
            bool: True if the entity's health status is 0 or less, False otherwise.
        """
        if max(self.status.get('health', 0), 0) == 0:
            return True
        return False   
