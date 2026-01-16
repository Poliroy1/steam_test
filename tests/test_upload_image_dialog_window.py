from pathlib import Path
from pages.upload_image_page import UploadImagePage

URL = "https://the-internet.herokuapp.com/upload"
FILE_NAME = "Image.PNG"
FILE_PATH = (Path("resources") / FILE_NAME).resolve()


def test_upload_image_via_dialog_window(browser):
    page = UploadImagePage(browser)

    browser.get(URL)
    page.wait_for_open()

    page.upload_file_via_dialog(str(FILE_PATH))

    assert page.has_dialog_file_name(), "Имя файла отображается на странице"
    assert page.has_success_status(), "Галочка отображается на странице"
