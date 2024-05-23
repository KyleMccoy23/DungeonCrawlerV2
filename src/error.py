from datetime import date

class GameError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

        self.filename = str(date.today())
        self.path = 'data\\logs'

        self.logError()

        print(f"An error has occurred : {message}")

        exit(1)

    def logError(self) -> None:
        with open(f'{self.path}\\{self.filename}.txt', 'a') as file:
            file.write(f"{self.__class__.__name__}: {self.message}\n")
