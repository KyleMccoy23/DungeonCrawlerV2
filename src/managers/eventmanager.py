


class EventManager:

    def __init__(self) -> None:
        self.lastEvent = 'init'

    def getLastEvent(self) -> str:
        return self.lastEvent
    
    def playerMove(self, direction:str, playerCords) -> tuple[int,int]:
        newCords = playerCords
        match(direction):
            case 'up':
                newCords[1] -= 1
            case 'down':
                newCords[1] += 1
            case 'left':
                newCords[0] -= 1
            case 'right':
                newCords[1] += 1
        cords = newCords
        
        self.lastEvent = 'playerMove'
        return cords