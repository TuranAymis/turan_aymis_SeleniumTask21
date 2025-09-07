from selenium.webdriver.common.action_chains import ActionChains
from pages.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class QaJobsPage(BasePage):
    URL = "https://useinsider.com/careers/quality-assurance/"

    seeAllQaJobsButton_css = (By.CSS_SELECTOR, "div[class='button-group d-flex flex-row']")
    filterLocation_xpath = (By.XPATH, "(//span[@class='select2-selection__rendered'])[1]")
    locationOption_xpath = (By.XPATH, "//li[text()='Istanbul, Turkiye']")
    filterDepartment_xpath = (By.XPATH, "(//span[@class='select2-selection__rendered'])[2]")
    departmentOptions_xpath = (By.XPATH, "//li[text()='Quality Assurance']")
    jobList_css = (By.CSS_SELECTOR, "div[id='jobs-list']")
    openPosition_xpath = (By.CSS_SELECTOR, "h3[class='mb-0']")
    jobName1_xpath = (By.XPATH, "(//p[@class='position-title font-weight-bold'])[1]")
    jobLocation1_xpath = (By.XPATH, "(//div[@class='position-location text-large'])[1]")
    jobName2_xpath = (By.XPATH, "(//p[@class='position-title font-weight-bold'])[2]")
    jobLocation2_xpath = (By.XPATH, "(//div[@class='position-location text-large'])[1]")
    wievRoleButton_xpath = (By.XPATH, "(//a[@class='btn btn-navy rounded pt-2 pr-5 pb-2 pl-5'])[2]")

    def __init__(self, driver):
        super().__init__(driver)

    def goQaPage(self):
        self.driver.get(self.URL)
        time.sleep(3)

    def clickSeeAllQaJobsButton(self):
        self.clickElement(self.seeAllQaJobsButton_css)
        time.sleep(5)

    def filterJobs(self):
        time.sleep(3)
        locationDropdown = self.waitElement(self.filterLocation_xpath)
        locationDropdown.click()
        locationTurkiye = self.waitElement(self.locationOption_xpath)
        locationTurkiye.click()
        time.sleep(3)
        departmentDropdown = self.waitElement(self.filterDepartment_xpath)
        departmentDropdown.click()
        departmentQA = self.waitElement(self.departmentOptions_xpath)
        departmentQA.click()
        time.sleep(3)

    def zoomOutPage(self):
        pageZoomOut = self.driver.execute_script("document.body.style.zoom='50%'")

    def scrollPage(self, y):
        scrollWindow = self.driver.execute_script("window.scrollTo(0, arguments[0]);", y)

    def scrollToJobsList(self):
        jobsListElement = self.waitElement(self.jobList_css)
        self.driver.execute_script("arguments[0].scrollIntoView();", jobsListElement)
        time.sleep(10)

    def verifyJobList(self):
        self.waitElement(self.jobList_css)
        jobList = self.driver.find_elements(*self.jobName1_xpath)
        assert len(jobList) > 0, "No positions available."

        for job in jobList:
            jobPosition1 = job.find_element(*self.jobName1_xpath)
            jobLocation1 = job.find_element(*self.jobLocation1_xpath)
            jobPosition2 = job.find_element(*self.jobName2_xpath)
            jobLocation2 = job.find_element(*self.jobLocation2_xpath)
            assert "Quality Assurance" in jobPosition1.text, "Pozisyon 'Quality Assurance' içermiyor."
            assert "Quality Assurance" in jobPosition2.text, "Pozisyon 'Quality Assurance' içermiyor."
            assert "Istanbul, Turkiye" in jobLocation1.text, "Pozisyon 'Istanbul, Turkiye' içermiyor."
            assert "Istanbul, Turkiye" in jobLocation2.text, "Pozisyon 'Istanbul, Turkiye' içermiyor."

    def hoverMouse(self):
        hoverElement = self.waitElement(self.jobName2_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(hoverElement).perform()

    def clickQaJobWievRole(self):
        clickWievRoleButton = self.waitElement(self.wievRoleButton_xpath)
        assert clickWievRoleButton, "No Wiev Role Button"
        clickWievRoleButton.click()
        
        self.driver.switch_to.window(self.driver.window_handles[1])

        time.sleep(3)

        return self.getUrl()