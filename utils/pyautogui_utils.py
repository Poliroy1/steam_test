import time
import pyautogui
import pyperclip

from logger.logger import Logger


class PyAutoGUIUtilities:
    @staticmethod
    def upload_file(file_path: str) -> None:
        Logger.info("Handle File Dialog for uploading file")
        time.sleep(3)

        Logger.debug(f"Copy '{file_path}' to clipboard")
        pyperclip.copy(file_path)

        Logger.debug("Paste path with Ctrl+V")
        pyautogui.hotkey('ctrl','v')

        Logger.debug("Press enter")
        pyautogui.press("enter")

        time.sleep(3)
