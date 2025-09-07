from pages.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class HomePage(BasePage):
    URL = "https://useinsider.com/"


    acceptCookie_css = (By.CSS_SELECTOR, "a[data-cli_action='accept_all']")
    companyButton_xpath = (By.XPATH, "(//a[@id='navbarDropdownMenuLink'])[5]")
    careerButton_xpath = (By.XPATH, "//a[text()='Careers']")

    def __init__(self, driver):
        super().__init__(driver)

    def goHomePage(self):
        self.driver.get(self.URL)

    def acceptCookie(self):
        try:
            self.clickElement(self.acceptCookie_css)
        except TimeoutException:
            print("Çerez kabul butonu bulunamadı, devam ediliyor.")

    def goCareersPage(self):
        self.clickElement(self.companyButton_xpath)
        self.clickElement(self.careerButton_xpath)
