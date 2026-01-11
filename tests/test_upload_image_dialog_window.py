from pathlib import Path
from pages.upload_image_page import UploadImagePage

url = "https://the-internet.herokuapp.com/upload"
file_name = "Image.png"

def test_upload_image_via_dialog_window(browser):
    page = UploadImagePage(browser)

    browser.get(url)
    page.wait_for_open()

    file_path = Path(__file__).parent.parent / "resources" / file_name

    page.upload_file_via_dialog(str(file_path))

    assert page.get_dialog_file_name().is_displayed()

    assert page.get_galochka().is_displayed()