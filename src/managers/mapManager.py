import MAPS
import helperFuncs

class MapManager:
    def __init__(self) -> None:
        pass

    def draw(self, playerCords:tuple) -> None:
        player = playerCords
        helperFuncs.mapLines()
        for e, x in enumerate(MAPS.mapForest):
            for i, y in enumerate(x):
                if i == 0:
                    print('|    ', end='')
                if e == player[0] and i == player[1]: print('P', end='')
                else:print(y[0], end='')
                if i == 5:
                    print('    |')
        helperFuncs.mapLines()