import keyboard
from threading import Thread
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.ProcessHandler.services.screen import CommandHandler

from modules.ProcessHandler.tools.exceptions import (
    ListenerCommandNotFoundError,
    AlreadyListeningError
)

class ListenerCommands(Enum):
    CHECK_PRESSED = "check_pressed"

class Listener:
    
    def __init__(self, command_handler:'CommandHandler') -> None:
        self.command_handler = command_handler
        self.func_thread:Thread = None
        self.listen_running = False

        self.commands = ListenerCommands

        self.command_attrs = {
            "check_pressed": {
                "key": "q"
            }
        }

    def listen(self, command_name:str):
        if self.func_thread is not None:
            raise AlreadyListeningError

        func = getattr(self, command_name)
        if func is None:
            raise ListenerCommandNotFoundError(command_name)

        self.listen_running = True
        self.func_thread = Thread(target=func)
        self.func_thread.start()

    def stop_listen(self):
        self.listen_running = False
        self.func_thread.join()
        self.func_thread = None

    def check_pressed(self):
        
        while self.listen_running:
            try:
                if keyboard.is_pressed(self.command_attrs["check_pressed"]["key"]):
                    self.command_handler.stop(from_listener=True)
                    self.stop_listen()
                    break
            except:
                break