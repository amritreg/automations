from selenium.webdriver.support.ui import Select
import os, sys
sys.path.insert(0, os.path.abspath(".."))
from Base import loggedInBaseTestCase

class CustomerNameTransactionIdStatusTestCase(loggedInBaseTestCase.LoggedInBaseTestCase):

	def test_CustomerNameTransactionIdStatus(self):
		self._caseId = 251
		self._suiteId = 2
		self._user = "rumbu"
		self._password = "Test@123"

		driver = self.driver
		self.login()
		#current Url
		self.assertEqual(driver.current_url,"http://54.186.24.234/pages/dashboard")
		#Transaction Button Click
		driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/ul[1]/li[2]/a").click()
		
		#View Button Click
		driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/ul[1]/li[2]/ul/li[1]/a").click()


		#Search Search Filter Button Click
		driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div/div/a").click()

		#selecting Customer Name
		driver.find_element_by_id("Transaction").click()
		driver.find_element_by_xpath("//html/body/div[1]/div[2]/div/div[2]/div[1]/form/fieldset/div[2]/div[1]/div[1]/select/option[2]").click()
		driver.find_element_by_id("Search_CustomerName").send_keys("Sunil Lama")

		#selecting TransactionId 
		driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/form/fieldset/div[2]/div[1]/div[1]/select/option[3]").click()
		#inserting TransactionID
		driver.find_element_by_id("Search_TransactionId").send_keys("123456789")

		#selecting staus
		abcx = Select(driver.find_element_by_id("Transaction"))
		abcx.select_by_visible_text("Status")
		status = Select(driver.find_element_by_id("Search_Status"))
		status.select_by_visible_text('Pending')