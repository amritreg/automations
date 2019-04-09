from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import os, sys
sys.path.insert(0, os.path.abspath(".."))
from Base import loggedInBaseTestCase

class TransactionsViewCreatePageTitleTestCase(loggedInBaseTestCase.LoggedInBaseTestCase):

	def test_TransactionsViewCreatePageTitle(self):
		self._caseId = 142
		self._suiteId = 2
		self._user = "rumbu"
		self._password = "Test@123"

		driver = self.driver
		self.login()
		#current Url
		self.assertEqual(driver.current_url,"http://54.186.24.234/pages/dashboard")

		#Going To Transaction Menu
		driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/ul[1]/li[2]/a").click()
		#clicking the create Button
		driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/ul[1]/li[2]/ul/li[2]/a").click()

		#checking if there is navbar or not 
		driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]")
		
		#checking if there is title with view Transactions
		titleText = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/h4").text
		self.assertEqual(titleText,"Create Transactions")
			


