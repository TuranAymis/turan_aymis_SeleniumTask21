# qa_insider_project/conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driverSetUp():
    """
    Pytest fixture to set up and tear down the WebDriver instance.
    """
    # ChromeDriverManager kullanarak otomatik olarak en güncel Chrome sürücüsünü indir
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    # Testler bittikten sonra tarayıcıyı kapat
    driver.quit()