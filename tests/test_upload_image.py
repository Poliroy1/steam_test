from pathlib import Path
from pages.upload_image_page import UploadImagePage

URL = "https://the-internet.herokuapp.com/upload"
FILE_NAME = "Image.PNG"
FILE_PATH = (Path("resources") / FILE_NAME).resolve()


def test_upload_image(browser):
    page = UploadImagePage(browser)

    browser.get(URL)
    page.wait_for_open()

    page.upload_file_click(str(FILE_PATH))

    actual_rs = page.get_upload_text()
    expected_rs = "File Uploaded!"
    assert expected_rs == actual_rs, f"Ожидали имя на странице: {expected_rs}, получили: {actual_rs}"

    assert page.get_file_name() == FILE_NAME, \
        f"Ожидалось имя файла '{FILE_NAME}', отображается '{page.get_file_name()}'"
