
from elements.button import Button
from elements.input import Input
from elements.label import Label
from logger.logger import Logger
from pages.base_page import BasePage

class UploadImagePage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//*[contains(text(),'File Uploader')]"
    FILE_INPUT = "file-upload"
    UPLOAD_BUTTON = "//input[@id='file-submit']"
    SUCCESS_TEXT = "//h3[text()='File Uploaded!']"
    FILE_NAME = "uploaded-files"
    DIALOG_WINDOW =''


    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = 'upload_image_page'

        self.unique_element = Label(self.browser, self.UNIQUE_ELEMENT_LOC, description='Unique element -> Label')
        self.file_input = Input(browser, self.FILE_INPUT, description="File Input -> Input")
        self.upload_button = Button(browser, self.UPLOAD_BUTTON, description='Upload button -> Button')
        self.file_name = Label(browser, self.FILE_NAME, description="Uploaded file name -> Label")
        self.success_text = Label(browser, self.SUCCESS_TEXT, description="Success text -> Label")

    def upload_file(self, file_path: str):
        Logger.info(f"{self}: upload file {file_path}")
        self.file_input.send_keys(file_path)
        self.upload_button.click()

