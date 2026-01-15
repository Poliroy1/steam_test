from pathlib import Path
from pages.upload_image_page import UploadImagePage

URL = "https://the-internet.herokuapp.com/upload"
file_name = "Image.PNG"


def test_upload_image_via_dialog_window(browser):
    page = UploadImagePage(browser)

    browser.get(URL)
    page.wait_for_open()

    file_path = (Path("resources") / file_name).resolve()

    page.upload_file_via_dialog(str(file_path))

    image_name = page.get_dialog_file_name()

    galochka = page.get_galochka()

    assert image_name.is_displayed(), f"Имя файла отображается на странице"

    assert galochka.is_displayed(), f"Галочка отображается на странице"
