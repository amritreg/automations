from abc import ABCMeta, abstractmethod
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest
import datetime
import testRailApi
import redmineApi

class BaseTestCase(unittest.TestCase):

    __metaclass__ = ABCMeta

    _baseUrl = None
    _caseId = None
    _runId = None
    _suiteId = None
    _issueId = None
    _projectId = None
    driver = None
    runs = None
    issue = None
    testrailapi = None
    redmineapi = None
    error_count = 0
    failure_count = 0
    current_datetime = None
    
    def setUp(self):

        self._caseId = None
        self._suiteId = None
        self._issueId = None
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self._baseUrl = "http://54.186.24.234"
        self._projectId = 1
        self.testrailapi = testRailApi.TestRailApi("https://vericheck.testrail.com/","","")
        self.redmineapi = redmineApi.RedmineApi("http://tickets.evericheck.com./","","")

    # def tearDown(self):
    #     self.driver.quit()

    def run(self, result):
        super(BaseTestCase, self).run(result)

        new_failure_count = len(result.failures)
        new_error_count = len(result.errors)

        if new_error_count > BaseTestCase.error_count:
            BaseTestCase.error_count = new_error_count
            msg = self.strErrorList('ERROR', result.errors[-1:])
            testResult = {'status_id': 5,'comment': msg}
        elif new_failure_count > BaseTestCase.failure_count:
            BaseTestCase.failure_count = new_failure_count
            msg = self.strErrorList('FAIL', result.failures[-1:])
            testResult = {'status_id': 5,'comment': msg}
            
        else:
            testResult = {'status_id': 1,'comment':'Success'}
    
        self.runs = self.testrailapi.getRunIdForCase(self._projectId,self._suiteId)
        self._runId = self.runs[0]['id']
        
        if not self._caseId:
            print "\n" + "Cannot Connect to TestRail Case ID required"
        elif not self._runId:
            print "\n" + 'Cannot Connect to TestRail Run ID required'
        else:
             #self.manageApi(testResult)
             print 123
       
    def manageApi(self, testResult):
        issue = self.testrailapi.getResultForCase(self._runId, self._caseId)
        subject = self.__class__.__name__[:-8] + ' - Selenium Test'

        if not issue['defects'] and testResult['status_id'] == 5:
            self._issueId = self.redmineapi.createIssue(subject, issue['url'])
        else:
            self._issueId = issue['defects']

        print self._issueId

        testResult['defects'] = str(self._issueId)
        self.testrailapi.addResultForCase(self._runId, self._caseId, testResult)

        if not issue['url'] and testResult['status_id'] == 5:
            updatedIssue = self.testrailapi.getResultForCase(self._runId, self._caseId)
            self.redmineapi.updateIssue(self._issueId, updatedIssue['url'])

    def strErrorList(self, flavour, errors):
	out = ''
        for test, err in errors:
            out += '======================================================================\n'
            out += "%s: %s\n" % (flavour, str(test))
            out += '----------------------------------------------------------------------\n'
            out += str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "\n"
            out += '----------------------------------------------------------------------\n'
            out += "%s\n" % err

        return out

