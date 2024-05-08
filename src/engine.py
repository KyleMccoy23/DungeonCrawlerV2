
from player import Player
from helperFuncs import clear


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

    def start(self) -> None:
        """
        Starts the game.

        """
        print("The game has started", end=" >>")
        input()
        print(self.player)