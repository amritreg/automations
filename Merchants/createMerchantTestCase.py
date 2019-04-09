import os, sys
sys.path.insert(0, os.path.abspath(".."))
from Base import loggedInBaseTestCase

class CreateMerchantTestCase(loggedInBaseTestCase.LoggedInBaseTestCase):
    def test_createMerchantTestCase(self):
        self._caseId = 144
        self._suiteId = 3
        self._user = "Admin"
        self._password = "Adminpass@1"
        driver = self.driver

        self.login()
        self.assertEqual(driver.current_url, "http://54.186.24.234/pages/dashboard")

        driver.find_element_by_xpath('//*[@id="top"]/div/div[2]/ul[1]/li[3]/a').click()
        driver.find_element_by_id('merchantadd').click()

        driver.find_element_by_id("MerchantName").clear()
        driver.find_element_by_id("MerchantName").send_keys("Ramesh")

        driver.find_element_by_id("MerchantBackendMerchantId").clear()
        driver.find_element_by_id("MerchantBackendMerchantId").send_keys("1234")

        driver.find_element_by_id("MerchantPin").clear()
        driver.find_element_by_id("MerchantPin").send_keys("as1")

        driver.find_element_by_id("MerchantFederalTaxId").clear()
        driver.find_element_by_id("MerchantFederalTaxId").send_keys("45678")

        driver.find_element_by_id('MerchantCode1').click()

        driver.find_element_by_xpath('//*[@id="MerchantCreateForm"]/fieldset/div/div/div[3]/div/input').click()

        self.assertEqual(driver.current_url, "http://54.186.24.234/merchants")







