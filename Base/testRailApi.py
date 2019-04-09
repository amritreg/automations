import testrail

class TestRailApi():

	issue = {}

	def __init__(self, url, user, password):
	    self.client = testrail.APIClient(url)
	    self.client.user = user
	    self.client.password = password
		
	def addResultForCase(self, runId, caseId, testResult):
	    self.client.send_post("add_result_for_case/"+ str(runId) + "/" + str(caseId), testResult)

	def getRunIdForCase(self, projectId, suiteId):
	    return self.client.send_get("get_runs/"+ str(projectId) + "&suite_id=" + str(suiteId) + "&is_completed=0")

	def getResultForCase(self, runId, caseId):
	    result = self.client.send_get("get_results_for_case/"+ str(runId) + "/" + str(caseId))
	    
	    if not result:
	    	self.issue['defects'] = None
	    	self.issue['url'] = None
	    else:
	    	self.issue['defects'] = result[0]['defects']
	    	self.issue['url'] = 'https://vericheck.testrail.com/index.php?/tests/view/' + str(result[0]['test_id'])

	    return self.issue
	    