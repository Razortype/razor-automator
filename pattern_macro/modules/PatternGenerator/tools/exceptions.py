
class PatternDuplicateError(Exception):
    
    def __init__(self, pattern_name, *args: object) -> None:
        super().__init__(*args)
        self.pattern_name = pattern_name

    def __str__(self) -> str:
        return f'Pattern name duplicated : {self.pattern_name}'

class PatternNullExceptionError(Exception):
    def __init__(self, pattern_name, *args: object) -> None:
        super().__init__(*args)
        self.patter_name = pattern_name

    def __str__(self) -> str:
        return f"Pattern not exists: {self.patter_name}"

class AutomationFunctionNotExistsError(Exception):

    def __init__(self, func_name, *args: object) -> None:
        super().__init__(*args)
        self.func_name = func_name

    def __str__(self) -> str:
        return f"Declared function name not exists: {self.func_name}"