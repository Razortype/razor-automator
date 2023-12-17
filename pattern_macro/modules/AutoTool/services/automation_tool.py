import pyautogui
import time

from typing import Tuple, List, TYPE_CHECKING

from common.Utils.types import X,Y,W,H

class BasicAutomations:
    
    @classmethod
    def move_cursor_to_mid(cls):
        w, h = cls.get_screen_size()
        cls.move_cursor_to((w//2, h//2))

    @staticmethod
    def get_screen_size() -> Tuple[W,H]:
        screenWidth, screenHeight = pyautogui.size()
        return (screenWidth, screenHeight)

    @staticmethod
    def click(position:Tuple[X,Y]=None, clicks=1):
        if position is None:
            pyautogui.click()
            return
        x, y = position
        pyautogui.click(x, y, clicks=clicks)

    @staticmethod
    def double_click(position:Tuple[X,Y]=None):
        if position is None:
            pyautogui.doubleClick()
            return
        x, y = position
        pyautogui.doubleClick(x, y)

    @staticmethod
    def mouse_down(button:str='left'):
        pyautogui.mouseDown(button=button)

    @staticmethod
    def mouse_up(button:str='left'):
        pyautogui.mouseUp(button=button)

    @staticmethod
    def move_cursor_to(position:Tuple[X,Y]):
        x, y = position
        pyautogui.moveTo(x, y)

    @staticmethod
    def press(key):
        pyautogui.press(key)

    @staticmethod
    def key_down(key):
        pyautogui.keyDown(key)

    @staticmethod
    def key_up(key):
        pyautogui.keyUp(key)

    @staticmethod
    def write(message:str, interval:float=0.25):
        pyautogui.write(message=message, interval=interval)

    @staticmethod
    def hotkey(keys):
        pyautogui.hotkey(*keys)

    @staticmethod
    def wait(second:float=1):
        time.sleep(second)

class ComplexAutomations:
    
    @classmethod
    def move_to_image(cls, asset_name):
        pass

    @classmethod
    def locate_and_click_all(cls, asset_name):
        pass

    @classmethod
    def locate_and_click(cls, asset_name):
        pass

    @classmethod
    def locate_and_hotkey(cls, asset_name, *keys):
        pass

    @staticmethod
    def hold_and_press(hold:str, *keys:List[str]):
        pass