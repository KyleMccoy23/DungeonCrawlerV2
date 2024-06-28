import MAPS

class MapManager:
    def __init__(self) -> None:
        pass

    def draw(self, playerCords:tuple) -> None:
        player = playerCords
        for e, x in enumerate(MAPS.mapForest):
            for i, y in enumerate(x):
                if e == player[0] and i == player[1]: print('P' if i!=5 else 'P\n', end='')
                else:print(y[0], end='')