import os
from error import GameError

help_lib = {
    'error':'Shows a discription | log location and log format',
    'h' : 'shows this page',
}

def clear() -> None:
    os.system('cls' if os.name == 'nt' else "clear")

def bannerLines() -> None:
    print('Xx---------------------xX')

def mapLines() -> None:
    print('Xx------------xX')


def gameHelp() -> None:
    while True:
        clear()
        bannerLines()
        print("This is For Game Help")
        print("For help menu enter 'h'") 
        bannerLines()
        query = input(">> ").lower()
        
        match query:
            case 'q':
                return
            case 'h':
                for key in help_lib.keys():
                    print(f" {key} : {help_lib.get(key)}")
            case 'error':
                tmp = GameError('', None, run=False)
                print(tmp.__str__())
                del tmp
            case _:
                continue
        input('>> ')
