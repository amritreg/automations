from selenium.webdriver.support.ui import Select
import os, sys
sys.path.insert(0, os.path.abspath(".."))
from Base import loggedInBaseTestCase

class EmptyRoutingNumberCreateAndContinueTestCase(loggedInBaseTestCase.LoggedInBaseTestCase):

	def test_EmptyRoutingNumberCreateAndContinue(self):
		self._caseId = 136
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

		#inserting value  in Customer Name
		driver.find_element_by_id("TransactionCustomerName").send_keys("AmritRegmi")

		#inserting value in description
		driver.find_element_by_id("TransactionDescription").send_keys("This is Descriptopn")

		#inserting value in Routing Number 
		driver.find_element_by_id("TransactionRoutingNumber").send_keys("")

		#inserting Value In Amount 
		driver.find_element_by_id("TransactionAmount").send_keys("234")

		#inserting value in Sec Code
		transactions_entry_class = Select(driver.find_element_by_id("TransactionEntryClass"))
		transactions_entry_class.select_by_visible_text("PPD")

		#inserting value in Account Number
		driver.find_element_by_id("TransactionAccountNumber").send_keys("123456789")

		#CLicking the botton create and continue
		driver.find_element_by_id("createNext").click()

		#check if its in same link
		self.assertEqual(driver.current_url,"http://54.186.24.234/transactions/create")