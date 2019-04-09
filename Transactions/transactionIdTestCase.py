import os, sys
sys.path.insert(0, os.path.abspath(".."))
from Base import loggedInBaseTestCase


class TransactionIdTestCase(loggedInBaseTestCase.LoggedInBaseTestCase):

	def test_TransactionId(self):
		self._caseId = 242
		self._suiteId = 2
		self._user = "rumbu"
		self._password = "Test@123"

		driver = self.driver
		self.login()
		self.assertEqual(driver.current_url,"http://54.186.24.234/pages/dashboard")


		driver.find_element_by_xpath("//html/body/div[1]/header/div/div[2]/ul[1]/li[6]/a").click()
		driver.find_element_by_xpath("//html/body/div[1]/header/div/div[2]/ul[1]/li[6]/ul/li[1]/a").click()
		


