from datetime import date

class GameError(Exception):
    def __init__(self, message: str, function, *, run:bool = True) -> None:

        self.filename = str(date.today())
        self.path = 'data\\logs'

        if run is not True:
            return
        super().__init__(message)
        self.message = message

        self.func = function

        self.logError()

        print(f"An error has occurred : {message}")

        exit(1)

    def logError(self) -> None:
        msgToWrite = f"{self.__class__.__name__}: {self.message}\n"
        if self.func is not None:
            msgToWrite = f"{self.__class__.__name__}: from {self.func.__qualname__} | {self.message}\n"

        with open(f'{self.path}\\{self.filename}.txt', 'a') as file:
            file.write(msgToWrite)

    def __str__(self) -> str:
        return f'An Error method that returns error message and logs the error\n\t* Errors logged in: {self.path}\n\t* Log format: "ERRORTYPE: from FUNCTION | MESSAGE"'