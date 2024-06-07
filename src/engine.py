
from error import GameError
from fileManager import FileManager
from player import Player
from helperFuncs import clear, bannerLines, gameHelp
from playerManager import PlayerManager


class Engine:

    def __init__(self) -> None:
        """
        Initializes a new instance of the `Engine` class.

        This method initializes the following instance variables:
        - `player`: An instance of the `Player` class.
        - `playerManager`: An instance of the `PlayerManager` class.
        - `fileManager`: An instance of the `FileManager` class.
        - `menu`: A boolean variable set to `False`.
        - `playing`: A boolean variable set to `False`.
        - `running`: A boolean variable set to `False`.

        This method does not take any parameters.

        This method does not return anything.
        """
        self.player = Player()
        self.playerManager = PlayerManager()
        self.fileManager = FileManager()

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
                player = self.fileManager.loadPlayer('Kyle')
                self.player = player
                self.menu = False
                self.playing = True

            case '3':
                gameHelp()
                self.menu = True
            
            case '4':
                exit(0)

    def play(self) -> None:
        print(self.player)
        self.fileManager.savePlayer(self.player)
        raise GameError("End Of Play loop", self.play)
