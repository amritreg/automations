import os, sys
from selenium.webdriver.support.ui import Select
sys.path.insert(0, os.path.abspath(".."))
from Base import loggedInBaseTestCase

class InvalidAmountTestCase(loggedInBaseTestCase.LoggedInBaseTestCase):
    def test_invalidAmount(self):
        self._caseId = 326
        self._suiteId = 8
        self._user = "rumbu"
        self._password = "Test@123"
        driver = self.driver

        self.login()
        self.assertEqual(driver.current_url, "http://54.186.24.234/pages/dashboard")

        driver.find_element_by_xpath('//*[@id="top"]/div/div[2]/ul[1]/li[3]/a').click()
        driver.find_element_by_xpath('//*[@id="top"]/div/div[2]/ul[1]/li[3]/ul/li[2]/a').click()

        amounts = ['0000', '-4444', '60000', 'This is invalid amount test']
        for amount in amounts:
            driver.find_element_by_id("CheckoutDescription").clear()
            driver.find_element_by_id("CheckoutDescription").send_keys("Ramesh kc")

            driver.find_element_by_id("CheckoutAmount").clear()
            driver.find_element_by_id("CheckoutAmount").send_keys(amount)

            checkout_standard_entry_class_id = Select(driver.find_element_by_id("CheckoutStandardEntryClassId"))
            checkout_standard_entry_class_id.select_by_visible_text("WEB")

            driver.find_element_by_xpath('//*[@id="CheckoutCreateForm"]/div[4]/div/div/input').click()

            self.assertEqual(driver.current_url, "http://54.186.24.234/checkouts/create")



