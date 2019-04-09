# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.abspath(".."))
from Base import loggedInBaseTestCase

class FooterCheckoutTestCase(loggedInBaseTestCase.LoggedInBaseTestCase):
    def test_footerCheckoutTestCase(self):
        self._caseId = 1461
        self._suiteId = 8
        self._user = "rumbu"
        self._password = "Test@123"
        driver = self.driver

        self.login()
        self.assertEqual(driver.current_url, "http://54.186.24.234/pages/dashboard")

        driver.find_element_by_xpath('//*[@id="top"]/div/div[2]/ul[1]/li[3]/a').click()
        driver.find_element_by_xpath('//*[@id="top"]/div/div[2]/ul[1]/li[3]/ul/li[1]/a').click()

        footer = driver.find_element_by_xpath('/html/body/footer/div').text
        footer_text = footer.encode('utf8')
        footer_text_given = "© Copyright 2015. All Rights Reserved."
        self.assertEqual(footer_text.strip(), footer_text_given)
        self.assertEqual(driver.current_url, "http://54.186.24.234/checkouts")


