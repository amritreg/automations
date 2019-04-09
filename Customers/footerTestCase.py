#-*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.abspath(".."))
from Base import loggedInBaseTestCase


class footerTestCase(loggedInBaseTestCase.LoggedInBaseTestCase):

	def test_footer(self):
		self._caseId = 1462
		self._suiteId = 33
		self._user = "rumbu"
		self._password = "Test@123"

		driver = self.driver
		self.login()

		self.assertEqual(driver.current_url,"http://54.186.24.234/pages/dashboard")
		driver.find_element_by_xpath("//html/body/div[1]/header/div/div[2]/ul[1]/li[4]/a").click()
		driver.find_element_by_xpath("//html/body/div[1]/header/div/div[2]/ul[1]/li[4]/ul/li[1]/a").click()
		
		if driver.find_element_by_xpath("/html/body/footer/div"):
			print 'Found Footer'
		# if footerText ==  string.find(self.driver.find_element_by_xpath("//html/body/footer/div").text): 
		# 	print 'Found The text'
		# else:
		# 	print 'Text Not Found'


		

		#footerText = self.driver.find_element_by_xpath("//html/body/footer/div").text
		#print footerText
		#unicodeData.encode('ascii', 'ignore')
		#self.assertTrue("Copyright 2014. All Rights Reserved. " in footerText )

		#self.assertEqual(driver.div,footerDiv)


		

		