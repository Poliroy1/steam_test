from pathlib import Path
from pages.upload_image_page import UploadImagePage

url = "https://the-internet.herokuapp.com/upload"
file_name = "Image.png"

def test_upload_image(browser):
    page = UploadImagePage(browser)

    browser.get(url)
    page.wait_for_open()

    file_path = Path(__file__).parent.parent / "resources" / file_name

    page.upload_file_click(str(file_path))

    assert "File Uploaded!" == page.get_upload_text()

    # Проверяем, что имя файла совпадает
    expected_file_name = file_name  # только имя файла
    assert page.get_file_name() == expected_file_name, \
        f"Ожидалось имя файла '{expected_file_name}', но отображается '{page.get_file_name()}'"


