
from http.client import UnimplementedFileMode
from player import Player

class Enemy(Player):

    def __init__(self) -> None:
        raise NotImplementedError('ENEMY DONT EXIST')
        super().__init__()