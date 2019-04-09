import os, sys
sys.path.insert(0, os.path.abspath(".."))
from Base import loggedInBaseTestCase

class CustomerNameTransactionIdTestCase(loggedInBaseTestCase.LoggedInBaseTestCase):

	def test_CustomerNameTransactionId(self):
		self._caseId = 245
		self._suiteId = 2
		self._user = "rumbu"
		self._password = "Test@123"

		driver = self.driver
		self.login()
		#current Url
		self.assertEqual(driver.current_url,"http://54.186.24.234/pages/dashboard")
		
		#Transaction Button Click
		driver.find_element_by_xpath("//html/body/div[1]/header/div/div[2]/ul[1]/li[2]/a").click()
		
		#View Button Click
		driver.find_element_by_xpath("//html/body/div[1]/header/div/div[2]/ul[1]/li[2]/ul/li[1]/a").click()
		
		#Search Filter Button Click
		driver.find_element_by_xpath("//html/body/div[1]/div[2]/div/div[2]/div[1]/div/div/a").click()

		#Add Filter Text Box Click
		driver.find_element_by_id("Transaction").click()

		driver.find_element_by_xpath("//html/body/div[1]/div[2]/div/div[2]/div[1]/form/fieldset/div[2]/div[1]/div[1]/select/option[2]").click()
		driver.find_element_by_id("Search_CustomerName").send_keys("Sunil Lama")
		driver.find_element_by_xpath("//html/body/div[1]/div[2]/div/div[2]/div[1]/form/fieldset/div[2]/div[1]/div[1]/select/option[3]").click()
		driver.find_element_by_id("Search_TransactionId").send_keys("24354747")

		#Search Filter Button Click
		driver.find_element_by_xpath("//html/body/div[1]/div[2]/div/div[2]/div[1]/form/fieldset/div[2]/div[3]/div/input").click()

		bodyText = self.driver.find_element_by_tag_name('body').text
		self.assertTrue("View Transactions" in bodyText)
		
