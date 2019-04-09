import baseTestCase

class LoggedInBaseTestCase(baseTestCase.BaseTestCase):

        _user = None

        _password = None

        def login(self):
            driver = self.driver
            driver.get(self._baseUrl + "/")
            driver.find_element_by_id("UserName").clear()
            driver.find_element_by_id("UserName").send_keys(self._user)
            driver.find_element_by_id("UserPassword").clear()
            driver.find_element_by_id("UserPassword").send_keys(self._password)
            driver.find_element_by_css_selector("input.btn.btn-danger").click()