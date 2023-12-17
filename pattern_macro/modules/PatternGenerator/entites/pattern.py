from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from modules.ProcessHandler.services.screen import CommandHandler

class PatternPiece:
    
    def __init__(self, index, func, func_kwargs, times) -> None:
        self.index = index
        self.func = func
        self.func_kwargs = func_kwargs
        self.times = times

    def execute(self):

        for _ in range(self.times):
            self.func(**self.func_kwargs)

class Pattern:
    
    def __init__(self, pattern_name:str, times:int, pieces:List[PatternPiece]) -> None:
        self.pattern_name = pattern_name
        self.times = times
        self.pieces = pieces

        self.running = False

    def start(self):

        self.running = True
        if self.times != "inf":
            for _ in range(self.times):
                self.execute_all()
            return
        
        while self.running:
            self.execute_all()

        self.running = False
        

    def execute_all(self):
        for piece in self.pieces:
            if not self.running:
                break
            piece.execute()