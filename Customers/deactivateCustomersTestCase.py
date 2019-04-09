import os, sys
sys.path.insert(0, os.path.abspath(".."))
from Base import loggedInBaseTestCase


class deactivateCustomersTestCase(loggedInBaseTestCase.LoggedInBaseTestCase):

	def test_deactivateCustomers(self):
		self._caseId = 1471
		self._suiteId = 33
		self._user = "rumbu"
		self._password = "Test@123"

		driver = self.driver
		self.login()

		self.assertEqual(driver.current_url,"http://54.186.24.234/pages/dashboard")
		driver.find_element_by_xpath("//html/body/div[1]/header/div/div[2]/ul[1]/li[4]/a").click()
		driver.find_element_by_xpath("//html/body/div[1]/header/div/div[2]/ul[1]/li[4]/ul/li[1]/a").click()
		driver.find_element_by_xpath("//html/body/div[1]/div[2]/div/div[2]/table/tbody/tr[2]/td[4]/a").click()
		
		#self.assertEqual((driver.find_element_by_xpath("//html/body/div[1]/div[2]/div/div[1]/font")).text,"*Customer has been deactivated.")

		bodyText = self.driver.find_element_by_tag_name('body').text
		self.assertTrue("*Customer has been deactivated." in bodyText)
