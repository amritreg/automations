import os, sys
sys.path.insert(0, os.path.abspath(".."))
from Base import loggedInBaseTestCase

class EnterValidInFormationThePaymentUrlTestCase(loggedInBaseTestCase.LoggedInBaseTestCase):
    def test_enterValidInFormationThePaymentUrl(self):
        self._caseId = 285
        self._suiteId = 8
        self._user = "rumbu"
        self._password = "Test@123"
        driver = self.driver

        self.login()
        self.assertEqual(driver.current_url, "http://54.186.24.234/pages/dashboard")

        driver.find_element_by_xpath('//*[@id="top"]/div/div[2]/ul[1]/li[3]/a').click()
        driver.find_element_by_xpath('//*[@id="top"]/div/div[2]/ul[1]/li[3]/ul/li[1]/a').click()
        driver.find_element_by_xpath('//*[@id="chekoutsTable"]/tbody/tr[1]/td[3]/a').click()

        driver.find_element_by_id("cname").clear()
        driver.find_element_by_id("cname").send_keys("Ramesh KC")

        driver.find_element_by_id("emailAdd").clear()
        driver.find_element_by_id("emailAdd").send_keys("kcramesh8@gmail.com")

        driver.find_element_by_id("route_num").clear()
        driver.find_element_by_id("route_num").send_keys("122105155")

        driver.find_element_by_id("acco_num").clear()
        driver.find_element_by_id("acco_num").send_keys("123456789")

        driver.find_element_by_id('CheckoutBankAccountTypeC').is_selected()

        driver.find_element_by_xpath('//*[@id="checkForm"]/div[2]/div[6]/div/a').click()

        if driver.find_element_by_xpath('//*[@id="chekoutsTable"]/tbody/tr[1]/td[4]/a'):
            driver.find_element_by_xpath('//*[@id="chekoutsTable"]/tbody/tr[2]/td[3]/a')
            print "Books Deactivate Button and Books URL found in Checkouts Function"

