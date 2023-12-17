
class ListenerCommandNotFoundError(Exception):
    def __init__(self, command_name, *args: object) -> None:
        super().__init__(*args)
        self.command_name = command_name

    def __str__(self) -> str:
        return f"Listener command not exists: {self.command_name}"
    
class AlreadyListeningError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return "Listener already listenin a function"