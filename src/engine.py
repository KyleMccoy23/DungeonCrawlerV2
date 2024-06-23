
from error import GameError
from managers import EventManager, PlayerManager, FileManager
from player import Player
from helperFuncs import clear, bannerLines, gameHelp


class Engine:

    def __init__(self) -> None:

        self.player = Player()
        self.playerManager = PlayerManager()
        self.fileManager = FileManager()
        self.eventManager = EventManager() 

        self.menu = False
        self.playing = False
        self.running = False
        

    def start(self) -> None:
        """
        Starts the game by printing a message to the console, waiting for the user to press 'enter' or 'return', and setting the `running` and `menu` attributes to `True`.

        This function does not take any parameters.

        This function does not return anything.
        """
        print("The game has started \nPress 'enter' or 'return' to start", end=" >>")
        input()
        
        self.running = True
        self.menu = True


    def run(self) -> None:
        
        while self.running:

            while self.menu:
                self.mainMenu()

            while self.playing:
                self.play()

    def mainMenu(self) -> None:

        clear()

        bannerLines()
        print('1. New Game')
        print('2. Load Game')
        print('3. Help')
        print('4. Quit')
        bannerLines()

        choice = input('# ')

        match(choice):
            case '1':
                self.player = self.playerManager.newPlayer()
                self.menu = False
                self.playing = True

            case '2':
                saves = self.fileManager.getSaveNames()
                for i, name in enumerate(saves):
                    print(f'{i+1} : {name}')
                save:int = int(input('# '))
                player = self.fileManager.loadPlayer(saves[(save-1)])
                self.player = player
                print(self.player)
                self.fileManager.savePlayer(self.player)
                for bar in self.player.bars:
                    bar.draw()
                input(">> ")
                self.menu = False
                self.playing = True

            case '3':
                gameHelp()
                self.menu = True
            
            case '4':
                exit(0)

    def play(self) -> None:
        pass

