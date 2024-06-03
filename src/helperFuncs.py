from config import *
from error import GameError

def clear() -> None:
    os.system('cls' if os.name == 'nt' else "clear")

def bannerLines() -> None:
    print('Xx---------------------xX')


def gameHelp() -> None:
    while True:
        clear()
        bannerLines()
        print("This is For Game Help")
        print("For help menu enter 'h'") 
        bannerLines()
        query = input(">> ")
        
        match query:
            case 'q':
                return
            case 'h':
                raise GameError("Help menu not implemented", gameHelp)
            case _:
                continue

