from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def waitElement(self, byLocator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(byLocator))
    
    def clickElement(self, byLocator):
        self.waitElement(byLocator).click()

    def getPageTitle(self):
        return self.driver.title
    
    def getUrl(self):
        return self.driver.current_url

    