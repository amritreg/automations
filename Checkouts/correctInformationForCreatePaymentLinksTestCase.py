import os, sys
from selenium.webdriver.support.ui import Select
sys.path.insert(0, os.path.abspath(".."))
from Base import loggedInBaseTestCase

class CorrectInformationForCreatePaymentLinksTestCase(loggedInBaseTestCase.LoggedInBaseTestCase):
    def test_correctInformationForCreatePaymentLinks(self):
        self._caseId = 293
        self._suiteId = 8
        self._user = "rumbu"
        self._password = "Test@123"
        driver = self.driver

        self.login()
        self.assertEqual(driver.current_url, "http://54.186.24.234/pages/dashboard")

        driver.find_element_by_xpath('//*[@id="top"]/div/div[2]/ul[1]/li[3]/a').click()
        driver.find_element_by_xpath('//*[@id="top"]/div/div[2]/ul[1]/li[3]/ul/li[2]/a').click()

        driver.find_element_by_id("CheckoutDescription").clear()
        driver.find_element_by_id("CheckoutDescription").send_keys("Ramesh")

        driver.find_element_by_id("CheckoutAmount").clear()
        driver.find_element_by_id("CheckoutAmount").send_keys("1234")

        checkout_standard_entry_class_id = Select(driver.find_element_by_id("CheckoutStandardEntryClassId"))
        checkout_standard_entry_class_id.select_by_visible_text("WEB")

        driver.find_element_by_xpath('//*[@id="CheckoutCreateForm"]/div[4]/div/div/input').click()

        self.assertEqual(driver.current_url, "http://54.186.24.234/checkouts")

        if driver.find_element_by_xpath('//*[@id="chekoutsTable"]/tbody/tr[1]/td[4]/a'):
            print "Books Deactivate Button Checkouts Function Found"
        if driver.find_element_by_xpath('//*[@id="chekoutsTable"]/tbody/tr[2]/td[3]/a'):
            print "Books links Checkouts Function found"








