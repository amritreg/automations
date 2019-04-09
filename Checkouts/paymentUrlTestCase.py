import os, sys
sys.path.insert(0, os.path.abspath(".."))
from Base import loggedInBaseTestCase

class PaymentUrlTestCase(loggedInBaseTestCase.LoggedInBaseTestCase):
    def test_paymentUrl(self):
        self._caseId = 284
        self._suiteId = 8
        self._user = "rumbu"
        self._password = "Test@123"
        driver = self.driver

        self.login()
        self.assertEqual(driver.current_url, "http://54.186.24.234/pages/dashboard")

        driver.find_element_by_xpath('//*[@id="top"]/div/div[2]/ul[1]/li[3]/a').click()
        driver.find_element_by_xpath('//*[@id="top"]/div/div[2]/ul[1]/li[3]/ul/li[1]/a').click()
        driver.find_element_by_xpath('//*[@id="chekoutsTable"]/tbody/tr[1]/td[3]/a').click()


