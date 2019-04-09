import os, sys
sys.path.insert(0, os.path.abspath(".."))
from Base import loggedInBaseTestCase


class viewCustomersTestCase(loggedInBaseTestCase.LoggedInBaseTestCase):

	def test_viewCustomers(self):
		self._caseId = 1470
		self._suiteId = 33
		self._user = "rumbu"
		self._password = "Test@123"

		driver = self.driver
		self.login()

		self.assertEqual(driver.current_url,"http://54.186.24.234/pages/dashboard")
		driver.find_element_by_xpath("//html/body/div[1]/header/div/div[2]/ul[1]/li[4]/a").click()
		driver.find_element_by_xpath("//html/body/div[1]/header/div/div[2]/ul[1]/li[4]/ul/li[1]/a").click()

		bodyText = self.driver.find_element_by_tag_name('body').text
		self.assertTrue("View Customers" in bodyText)
