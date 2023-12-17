from pick import pick

from typing import List, Tuple

def single_select_menu(
            options:List[Tuple[str,str]], 
            title:str="Pick one below"
            ) -> Tuple[Tuple[str, str], int]:
        _, index = pick([i[0] for i in options], title)
        return (options[index], index)

# def multiple_select_menu(*options):
#     terminal_menu = TerminalMenu(options)
#     menu_entry_index = terminal_menu.show()
#     pass