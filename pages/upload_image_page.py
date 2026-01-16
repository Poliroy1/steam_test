from elements.button import Button
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from logger.logger import Logger
from pages.base_page import BasePage

from utils.pyautogui_utils import PyAutoGUIUtilities


class UploadImagePage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//*[contains(text(),'File Uploader')]"
    FILE_INPUT = "file-upload"
    UPLOAD_BUTTON = "file-submit"
    SUCCESS_TEXT = "//h3[text()='File Uploaded!']"
    FILE_NAME = "uploaded-files"
    DIALOG_WINDOW = "drag-drop-upload"
    GALOCHKA = "//*[@id='drag-drop-upload']//*[contains(@class, 'dz-success-mark')]//span"
    DIALOG_FILE_NAME = "//*[contains(@class, 'dz-filename')]//span"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = 'upload_image_page'

        self.unique_element = Label(self.browser, self.UNIQUE_ELEMENT_LOC, description='Unique element -> Label')
        self.file_input = Input(self.browser, self.FILE_INPUT, description="File Input -> Input")
        self.upload_button = Button(self.browser, self.UPLOAD_BUTTON, description='Upload button -> Button')
        self.file_name = Label(self.browser, self.FILE_NAME, description="Uploaded file name -> Label")
        self.success_text = Label(self.browser, self.SUCCESS_TEXT, description="Success text -> Label")
        self.dialog_window = Label(self.browser, self.DIALOG_WINDOW, description="Dialog window -> Label")
        self.status = Label(self.browser, self.GALOCHKA, description="Galochka -> Label")
        self.dialog_file_name = Label(self.browser, self.DIALOG_FILE_NAME, description="Dialog file name -> Label")

    def upload_file_click(self, file_path: str):
        Logger.info(f"{self}: upload file {file_path}")
        self.file_input.send_keys(str(file_path))
        self.upload_button.click()

    def get_upload_text(self):
        Logger.info(f"{self}: get upload text")
        text = self.success_text.get_text()
        return text

    def get_file_name(self):
        Logger.info(f"{self}: get file name")
        text = self.file_name.get_text()
        return text

    def upload_file_via_dialog(self, file_path: str):
        Logger.info(f"{self}: upload file via dialog window")
        self.dialog_window.click()
        PyAutoGUIUtilities.upload_file(file_path)

    def get_dialog_file_name(self):
        Logger.info(f"{self}: get dialog file name")
        return self.dialog_file_name
