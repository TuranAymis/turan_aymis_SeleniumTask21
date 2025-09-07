from pages.basePage import BasePage
from selenium.webdriver.common.by import By

class CareersPage(BasePage):

    #Locations
    ourLocations_xpath = (By.XPATH, "//h3[@class='category-title-media ml-0']")
    locationNewYork_xpath = (By.XPATH, "(//p[@class='mb-0'])[1]")
    locationSaoPaulo_xpath = (By.XPATH, "(//p[@class='mb-0'])[2]")
    locationLondon_xpath = (By.XPATH, "(//p[@class='mb-0'])[3]")

    #Teams
    teamCustomerSuccess_xpath = (By.XPATH, "(//div[@class='job-title mt-0 mt-lg-2 mt-xl-5'])[1]")
    teamSales_xpath = (By.XPATH, "(//div[@class='job-title mt-0 mt-lg-2 mt-xl-5'])[2]")
    teamProductEngineering_xpath = (By.XPATH, "(//div[@class='job-title mt-0 mt-lg-2 mt-xl-5'])[3]")

    #Life At Insider
    lifeAtInsider_xpath = (By.XPATH, "//h2[text()='Life at Insider']")

    def __init__(self, driver):
        super().__init__(driver)

    def verifyCareersPageSections(self):
       elementsCheck = [
           self.locationNewYork_xpath,
           self.locationSaoPaulo_xpath,
           self.locationLondon_xpath,
           self.teamCustomerSuccess_xpath,
           self.teamSales_xpath,
           self.teamProductEngineering_xpath,
           self.lifeAtInsider_xpath
       ]
       for locator in elementsCheck:
           self.waitElement(locator)
