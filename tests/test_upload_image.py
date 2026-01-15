from pathlib import Path
from pages.upload_image_page import UploadImagePage

URL = "https://the-internet.herokuapp.com/upload"
file_name = "Image.PNG"


def test_upload_image(browser):
    page = UploadImagePage(browser)

    browser.get(URL)
    page.wait_for_open()

    file_path = (Path("resources") / file_name).resolve()

    page.upload_file_click(str(file_path))

    actual_rs = page.get_upload_text()
    expected_rs = "File Uploaded!"
    assert expected_rs == actual_rs, f"Ожидали имя на странице: {expected_rs}, получили: {actual_rs}"

    expected_file_name = file_name
    assert page.get_file_name() == expected_file_name, \
        f"Ожидалось имя файла '{expected_file_name}', отображается '{page.get_file_name()}'"
