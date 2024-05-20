
from error import GameError
from healthBar import healthBar, manaBar, staminaBar
from helperFuncs import clear, bannerLines
from player import Player

classes: list[str] = [
    "Fighter", 
    "Rogue", 
    "Wizard", 
    "Cleric", 
    "Ranger", 
    "Bard", 
    "Paladin", 
    "Barbarian", 
    "Monk", 
    "Sorcerer", 
    "Warlock", 
    "Druid"
]

races: list[str] = [
    "Human", 
    "Elf",
    "Dwarf", 
    "Halfling", 
    "Gnome", 
    "Half-Elf", 
    "Half-Orc", 
    "Tiefling", 
    "Dragonborn", 
    "Aasimar"
]


class PlayerManager:

    def __init__(self) -> None:
        pass

    
    def newPlayer(self) -> Player:

        self.player = Player()

        clear()
        bannerLines()        

        self.player.setInfo('name', input("Enter a Name for you character\n# "))

        clear()
        bannerLines()  
        print(self.player)

        self.player.setInfo('class', self.chooseClass())

        clear()
        bannerLines()  
        print(self.player)

        self.player.setInfo('race', self.chooseRace())
        
        clear()
        bannerLines()  
        print(self.player)

        bannerLines()
    
        return self.player

    def chooseClass(self) -> str:
        while True:
            for n, c in enumerate(classes):
                print(n+1, c)
            selectedClass = input('Enter your class(number)\n# ')
            if selectedClass != '':
                selectedClass = int(selectedClass)
                break
            clear()
        clear()
        return classes[selectedClass-1]

    def chooseRace(self) -> str:
        while True:
            for n, r in enumerate(races):
                print(n+1, r)
            selectedRace = input('Enter your race(number)\n# ')
            if selectedRace != '':
                selectedRace = int(selectedRace)
                break
            clear()
        clear()
        return races[selectedRace-1]

    def loadPlayer(self) -> Player:
        raise GameError('No Player Loading Defined')
