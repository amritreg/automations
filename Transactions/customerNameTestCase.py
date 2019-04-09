import os, sys
sys.path.insert(0, os.path.abspath(".."))
from Base import loggedInBaseTestCase

class CustomerNameTestCase(loggedInBaseTestCase.LoggedInBaseTestCase):

	def test_CustomerName(self):
		self._caseId = 241
		self._suiteId = 2
		self._user = "rumbu"
		self._password = "Test@123"

		driver = self.driver
		self.login()
		self.assertEqual(driver.current_url,"http://54.186.24.234/pages/dashboard")
		

		driver.find_element_by_xpath("//html/body/div[1]/header/div/div[2]/ul[1]/li[2]/a").click()
		driver.find_element_by_xpath("//html/body/div[1]/header/div/div[2]/ul[1]/li[2]/ul/li[1]/a").click()
		driver.find_element_by_xpath("//html/body/div[1]/div[2]/div/div[2]/div[1]/div/div/a").click()
		driver.find_element_by_id("Transaction").click()
		driver.find_element_by_xpath("//html/body/div[1]/div[2]/div/div[2]/div[1]/form/fieldset/div[2]/div[1]/div[1]/select/option[2]").click()
		driver.find_element_by_id("Search_CustomerName").send_keys("Asdfasdf")
		driver.find_element_by_xpath("//html/body/div[1]/div[2]/div/div[2]/div[1]/div/div/a").click()
		bodyText = self.driver.find_element_by_tag_name('body').text
		self.assertTrue("View Transactions" in bodyText)
