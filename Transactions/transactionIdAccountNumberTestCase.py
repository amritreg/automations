import os, sys
sys.path.insert(0, os.path.abspath(".."))
from Base import loggedInBaseTestCase

class TransactionIdAccountNumberTestCase(loggedInBaseTestCase.LoggedInBaseTestCase):

	def test_TransactionIdAccountNumber(self):
		self._caseId = 249
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

		#Search Filter Button Click
		driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div/div/a").click()

		#clicked on add filter Dropdown
		driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/form/fieldset/div[2]/div[1]/div[1]/select").click()

		#selecting TransactionId 
		driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/form/fieldset/div[2]/div[1]/div[1]/select/option[3]").click()
		#inserting TransactionID
		driver.find_element_by_id("Search_TransactionId").send_keys("123456789")

		#clicked on add filter Dropdown
		driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/form/fieldset/div[2]/div[1]/div[1]/select").click()
		#selecting Account Number
		driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/form/fieldset/div[2]/div[1]/div[1]/select/option[5]").click()
		#inserting Account Number
		driver.find_element_by_id("Search_AccountNumber").send_keys("123456789")
		
		#clicking in Apply Button 
		driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/form/fieldset/div[2]/div[3]/div/input").click()


		#chekich if its routing to its found Information 
		bodyText = self.driver.find_element_by_tag_name('body').text
		self.assertTrue("View Transactions" in bodyText)