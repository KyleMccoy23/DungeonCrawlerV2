from items import fists
from item import Item

class Entity:
    def __init__(self) -> None:

        self.defaultWeapon = fists
        
        self.info:dict[str, str] = {
            'name':'',
            'class':'',
            'race':'',
            'status':'',
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