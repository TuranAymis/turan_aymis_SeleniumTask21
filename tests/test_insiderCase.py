import pytest
from pages.careersPage import CareersPage
from pages.homePage import HomePage
from pages.qaJobsPage import QaJobsPage



def  test_insiderQaCase(driverSetUp):
    driver = driverSetUp

    #1. Visit https://useinsider.com/ and check Insider home page is opened or not
    pageHome = HomePage(driver)
    pageHome.goHomePage()
    pageHome.acceptCookie()
    assert "#1 Leader in Individualized, Cross-Channel CX — Insider" in pageHome.getPageTitle()

    #2. Select the “Company” menu in the navigation bar, select “Careers” and check Career page, its Locations, Teams, and Life at Insider blocks are open or not
    pageHome.goCareersPage()
    pageCareers = CareersPage(driver)
    pageCareers.verifyCareersPageSections()

    #3. Go to https://useinsider.com/careers/quality-assurance/, click “See all QA jobs”, filterjob s by Location: “Istanbul, Turkey”, and Department: “Quality Assurance”, check the presence of the jobs list
    pageQaJobs = QaJobsPage(driver)
    pageQaJobs.goQaPage()
    pageQaJobs.clickSeeAllQaJobsButton()
    pageQaJobs.scrollToJobsList()
    pageQaJobs.filterJobs()
    pageQaJobs.zoomOutPage()
    pageQaJobs.scrollPage(-10)

    #4. Check that all jobs’ Position contains “Quality Assurance”, Department contains “Quality Assurance”, and Location contains “Istanbul, Turkey”
    pageQaJobs.verifyJobList()
    pageQaJobs.hoverMouse()

    #5. Click the “View Role” button and check that this action redirects us to the Lever Application form page
    leverURL = pageQaJobs.clickQaJobWievRole()
    assert "jobs.lever.co" in leverURL, "jobs.lever.co bulunamadı. Mevcut URL: {leverURL} "

