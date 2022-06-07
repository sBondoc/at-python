from datetime import date, datetime, time
from subprocess import run
class Job(object):
	def __init__(self, command: str, at: datetime):
		self.command = command
		self.at = at
		self.scheduled = False
	def schedule(self):
		cmd = self.command
		t = self.at.strftime('%Y%m%d%H%M.%S')
		run(('at', '-t', t.encode()), input = cmd.encode())
		self.scheduled = True
