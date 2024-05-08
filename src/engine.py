
from player import Player
from helperFuncs import clear, bannerLines, gameHelp
from playerManager import PlayerManager


class Engine:
    """
    Represents the game engine responsible for managing game logic and interactions.

    This class initializes the game and provides methods to start and control the game flow.

    Attributes:
        None

    Methods:
        __init__: Initializes the game engine.
        start: Starts the game by prompting the user to press Enter and then printing the current state of the player character.
    """

    def __init__(self) -> None:
        """
        Initializes the game engine.

        This method sets up the initial state of the game engine.
        """
        # test
        self.player = Player() #⁡⁢⁣⁢ TO REMOVE⁡

        self.playerManager = PlayerManager()

        self.menu = False
        self.playing = False
        self.running = False
        

    def start(self) -> None:
        """
        Starts the game.

        """
        print("The game has started \nPress 'enter' or 'return' to start", end=" >>")
        input()
        
        self.running = True
        self.menu = True

        self.run()


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
                self.playerManager.newPlayer()
                self.menu = False
                self.playing = True

            case '2':
                self.playerManager.loadPlayer()
                self.menu = False
                self.playing = True

            case '3':
                gameHelp()
                self.menu = True
            
            case '4':
                exit(0)

    def play(self) -> None:
        pass