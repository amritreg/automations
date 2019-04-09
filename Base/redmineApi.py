from redmine import Redmine

class RedmineApi:


	def __init__(self, url, user, password):
	    self.redmine = Redmine(url, username=user, password=password)

	def createIssue(self, subject, description):
		issue = self.redmine.issue.create(project_id='Sourceopia', subject=subject, tracker_id=1, description=description, assigned_to_id=26)
		return issue.id

	def updateIssue(self, issueId, description):
		issue = self.redmine.issue.update(issueId, description= description)
		