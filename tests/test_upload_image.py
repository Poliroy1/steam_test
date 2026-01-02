import os
from pages.upload_image_page import UploadImagePage

def test_upload_image(browser):
    page = UploadImagePage(browser)

    browser.get('https://the-internet.herokuapp.com/upload')
    page.wait_for_open()

    file_path = os.path.abspath("resources/test_file.txt")
    file_name = os.path.basename(file_path)

    page.upload_file(file_path)

    page.success_text.wait_for_presence()

    assert page.success_text.is_displayed(), \
        "Ожидалась надпись 'File Uploaded!', но она не появилась"

    assert page.file_name.get_text() == file_name, \
        f"Ожидалось имя файла '{file_name}', но отображается '{page.file_name.get_text()}'"