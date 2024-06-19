
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

        self.player.setInfo('class', self.chooseClass())

        clear()

        self.player.setInfo('race', self.chooseRace())
        
        clear()

        self.setStats()

        bannerLines()
        
        self.updatePlayerinfo()
        self.updateBars()
    
        return self.player
    
    def updatePlayerinfo(self) -> None:
        self.player.setStatus('health', 10 + self.player.getStat('Con') * self.player.getStatus('level'))
        self.player.setStatus('maxHealth', self.player.getStatus('health'))
        self.player.setStatus('mana', 5 + self.player.getStat('Int') * self.player.getStatus('level'))
        self.player.setStatus('maxMana', self.player.getStatus('mana'))
        self.player.setStatus('stamina', 10 + (self.player.getStat('Con')*self.player.getStatus('level')) * self.player.getStatus('level'))
        self.player.setStatus('maxStamina', self.player.getStatus('stamina'))

    def updateBars(self) -> None:
        for bar in self.player.bars:
            bar.updateMax()
        
    def setStats(self) -> None:
        maxStats = 14
        for s in self.player.stats:
            tempStats = maxStats
            bannerLines()
            print("How many point do you want to put into your stats (Max is 10)")
            print(f"Remaining Stat Points: {maxStats}")
            for ss in self.player.stats:
                if self.player.stats[ss] > 0:
                    print(f'{ss} : {self.player.stats.get(ss)}')
            bannerLines()
            statPoints = input(f"{s} : ")
            if statPoints == '': statPoints = 1
            elif statPoints == 'q': exit(0)
            else: statPoints = int(statPoints)
            tempStats -= statPoints
            if tempStats < 0:
                self.player.setStat(s, maxStats)
                return
            elif statPoints == 1:
                tempStats += statPoints
                clear()
                continue
            self.player.setStat(s, statPoints)
            maxStats = tempStats + 1
            clear()

    def chooseClass(self) -> str:
        while True:
            bannerLines()
            for n, c in enumerate(classes):
                print(f'{n+1} : {c}')
            bannerLines()
            selectedClass = input('Enter your class(number)\n# ')
            if selectedClass != '':
                selectedClass = int(selectedClass)
                break
            clear()
        clear()
        return classes[selectedClass-1]

    def chooseRace(self) -> str:
        while True:
            bannerLines()
            for n, r in enumerate(races):
                print(f'{n+1} : {r}')
            bannerLines()
            selectedRace = input('Enter your race(number)\n# ')
            if selectedRace != '':
                selectedRace = int(selectedRace)
                break
            clear()
        clear()
        return races[selectedRace-1]
