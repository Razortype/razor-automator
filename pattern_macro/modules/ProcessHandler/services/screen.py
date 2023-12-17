from typing import List, Tuple
from threading import Thread

from modules.PatternGenerator.services.generator import PatternGenerator, Pattern

from modules.ProcessHandler.services.listener import Listener

from modules.ProcessHandler.tools.prints import MonitorPrints, CommandHandlerPrints
from modules.ProcessHandler.tools.tools import single_select_menu as _ssm

__all__ = ["Monitor"]

class CommandHandler:
    
    def __init__(self, pattern:Pattern) -> None:
        self.pattern = pattern
        self.process_running = False
        self.listener = Listener(self)
        self.pattern_thread:Thread = None

    def start(self):
        
        self.process_running = True
        print('type "help" to learn commands')
        while self.process_running:
            command = input("=> ")

            match command:
                case "start":
                    self.create_thread()
                case "stop":
                    self.stop()
                case "quit":
                    if self.pattern_thread is not None:
                        CommandHandlerPrints.quit_error()
                        continue
                    self.process_running = False
                case "help":
                    CommandHandlerPrints.help_section()
                case _:
                    CommandHandlerPrints.wrong_input()
    
    def stop(self, from_listener=False):

        if self.pattern_thread is None:
            CommandHandlerPrints.stop_error()
            return

        if not from_listener:
            self.listener.stop_listen()        
        self.pattern.running = False
        self.pattern_thread.join()
        self.pattern_thread = None

    def create_thread(self):

        if self.pattern_thread is not None:
            CommandHandlerPrints.start_error()
            return

        self.pattern_thread = Thread(target=self.pattern.start)
        self.pattern_thread.start()
        self.listener.listen(self.listener.commands.CHECK_PRESSED.value)

class Monitor:
    
    def __init__(self, pattern_handler:PatternGenerator) -> None:
        self.pattern_handler = pattern_handler
        
        self.program_running = True

    def start(self):
        
        MonitorPrints.start_screen()
        print('type "help" to learn commands')
        while self.program_running:
            command = input(":> ")

            match command:
                case "pick":
                    (_, picked), _ = _ssm(self.pattern_handler.get_registered())
                    pattern = self.pattern_handler.get_pattern(picked)
                    self.command_handler = CommandHandler(pattern)
                    self.command_handler.start()
                    self.command_handler = None

                case "help":
                    MonitorPrints.help_section()
                case "quit":
                    MonitorPrints.quit_message()
                    self.program_running = False