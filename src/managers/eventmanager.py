


class EventManager:

    def __init__(self) -> None:
        self.lastEvent = 'init'

    def getLastEvent(self) -> str:
        return self.lastEvent
    
    def playerMove(self, player) -> tuple[int,int]:
        cords = player.location.get('cords')
        self.lastEvent = 'playerMove'
        return cords