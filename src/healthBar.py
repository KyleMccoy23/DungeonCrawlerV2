
import os

from entity import Entity

os.system("")

class Bar:
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"
    colors: dict = {"red": "\033[91m",
                    "purple": "\33[95m",
                    "blue": "\33[34m",
                    "blue2": "\33[36m",
                    "blue3": "\33[96m",
                    "green": "\033[92m",
                    "green2": "\033[32m",
                    "brown": "\33[33m",
                    "yellow": "\33[93m",
                    "grey": "\33[37m",
                    "default": "\033[0m"
                    }

    def __init__(self,
                 length: int = 20,
                 is_colored: bool = True,
                 color: str = "") -> None:
        self.length = length
        self.max_value = 0
        self.current_value = 0

        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors["default"]

    def update(self) -> None:
        raise NotImplementedError("Update No updated")

    def barTitle(self) -> None:
        raise NotImplementedError("No Bar Title")

    def draw(self) -> None:
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        self.barTitle()
        print(f"{self.barrier}"
              f"{self.color if self.is_colored else ''}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colors['default'] if self.is_colored else ''}"
              f"{self.barrier}")
        
class healthBar(Bar):
    def __init__(self, 
                 entity:Entity, 
                 length: int = 20, 
                 is_colored: bool = True, 
                 color: str = "green2") -> None:
        super().__init__(length, is_colored, color)
        self.entity = entity
        self.max_value = entity.status.get('maxHealth')
        self.current_value = entity.status.get('health')

    def barTitle(self) -> None:
        print(f"{self.entity.identity.get('name')}'s HEALTH: {self.entity.status.get('health')}/{self.entity.status.get('maxHealth')}")

    def update(self) -> None:
        self.current_value = self.entity.status.get('health')

class manaBar(Bar):
    def __init__(self, 
                 entity:Entity, 
                 length: int = 20, 
                 is_colored: bool = True, 
                 color: str = "blue2") -> None:
        super().__init__(length, is_colored, color)
        self.entity = entity
        self.max_value = entity.status.get('maxMana')
        self.current_value = entity.status.get('mana')

    def barTitle(self) -> None:
        print(f"{self.entity.identity.get('name')}'s MANA: {self.entity.status.get('mana')}/{self.entity.status.get('maxMana')}")

    def update(self) -> None:
        self.current_value = self.entity.status.get('mana')

class staminaBar(Bar):
    def __init__(self, 
                 entity:Entity, 
                 length: int = 20, 
                 is_colored: bool = True, 
                 color: str = "green") -> None:
        super().__init__(length, is_colored, color)
        self.entity = entity
        self.max_value = entity.status.get('maxStamina')
        self.current_value = entity.status.get('stamina')

    def barTitle(self) -> None:
        print(f"{self.entity.info.get('name')}'s STAMINA: {self.entity.status.get('stamina')}/{self.entity.status.get('maxStamina')}")
    
    def update(self) -> None:
        self.current_value = self.entity.status.get('stamina')