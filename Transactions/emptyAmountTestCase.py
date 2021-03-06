from selenium.webdriver.support.ui import Select
import os, sys
sys.path.insert(0, os.path.abspath(".."))
from Base import loggedInBaseTestCase

class EmptyAmountTestCase(loggedInBaseTestCase.LoggedInBaseTestCase):

	def test_EmptyAmount(self):
		self._caseId = 123
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
		driver.find_element_by_id("TransactionCustomerName").send_keys("Amrit Regmi")

		#inserting value in description
		driver.find_element_by_id("TransactionDescription").send_keys("This is description")

		#inserting value in Routing Number 
		driver.find_element_by_id("TransactionRoutingNumber").send_keys("123456789")

		#inserting Value In Amount 
		driver.find_element_by_id("TransactionAmount").send_keys("")

		#inserting value in Sec Code
		transactions_entry_class = Select(driver.find_element_by_id("TransactionEntryClass"))
		transactions_entry_class.select_by_visible_text("PPD")

		#inserting value in Account Number
		driver.find_element_by_id("TransactionAccountNumber").send_keys("123456789")

		#CLicking the botton create
		driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/fieldset/div/div[6]/div[1]/div/input").click()

		#check if its in same link
		self.assertEqual(driver.current_url,"http://54.186.24.234/transactions/create")