from modules.PatternGenerator.entites.pattern import Pattern, PatternPiece
from modules.PatternGenerator.entites.intro import Intro

from modules.AutoTool.services.automation_tool import (
    BasicAutomations,
    ComplexAutomations
)

from modules.PatternGenerator.tools.exceptions import (
    PatternDuplicateError,
    PatternNullExceptionError,
    AutomationFunctionNotExistsError
)

from typing import Dict

class PatternGenerator:

    patterns = {}

    def enter_patterns(self, patterns:Dict[str, dict]):
        
        for pattern_name, context in patterns.items():
            pattern = self.generate_pattern(pattern_name, context)
            
            if pattern_name in self.patterns.keys():
                raise PatternDuplicateError(pattern_name)
            self.patterns[pattern_name] = pattern

    def generate_pattern(self, pattern_name:str, context:dict) -> Pattern:
        
        times = context.get("times", 1)
        
        pieces = []
        for index, piece_context in context["path"].items():
            piece = self.generate_piece(index, piece_context)
            pieces.append(piece)

        pattern = Pattern(
             pattern_name,
             times,
             pieces
        )

        return pattern
    
    def generate_piece(self, index:str, piece_context:dict) -> PatternPiece:
            func_name = piece_context["func"]
            
            basic_func = getattr(BasicAutomations, func_name, lambda: None)
            complex_func = getattr(ComplexAutomations, func_name, lambda: None)

            if basic_func is None and complex_func is None:
                raise AutomationFunctionNotExistsError(func_name)

            func = basic_func if basic_func else complex_func

            func_kwargs = piece_context.get("kwargs", {})
            times = piece_context.get("times", 1)
            return PatternPiece(index, func, func_kwargs, times)

    def get_registered(self):
         return [(i.replace("_", " ").title(),i) for i in list(self.patterns.keys())]
    
    def get_pattern(self, pattern_name:str) -> Pattern:
        pattern:Pattern = self.patterns.get(pattern_name, None)
        if pattern is None:
            raise PatternNullExceptionError(pattern_name)
        return pattern

pattern_handler = PatternGenerator()