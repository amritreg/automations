import os, sys
sys.path.insert(0, os.path.abspath(".."))
from Base import loggedInBaseTestCase

class CustomerNameTestCase(loggedInBaseTestCase.LoggedInBaseTestCase):

	def test_Status(self):
		self._caseId = 243
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

		#selecting Status 
		driver.find_element_by_xpath("//html/body/div[1]/div[2]/div/div[2]/div[1]/form/fieldset/div[2]/div[1]/div[1]/select/option[4]").click()

		#entering the status
		driver.find_element_by_xpath("//html/body/div[1]/div[2]/div/div[2]/div[1]/form/fieldset/div[2]/div[5]/div/div/div/select/option[1]").click

		#Search Filter Button Click
		driver.find_element_by_xpath("//html/body/div[1]/div[2]/div/div[2]/div[1]/div/div/a").click()

		bodyText = self.driver.find_element_by_tag_name('body').text
		self.assertTrue("View Transactions" in bodyText)



