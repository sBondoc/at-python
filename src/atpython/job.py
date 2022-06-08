from datetime import date, datetime, time
from subprocess import run
class Job(object):
	def __init__(self, command: str, at: datetime):
		self.command = command
		self.at = at
		self.scheduled = False
		self.number = -1
		self.raw = None
	def schedule(self):
		if not self.scheduled:
			cmd = self.command
			t = self.at.strftime('%Y%m%d%H%M.%S')
			run(('at', '-t', t.encode()), input = cmd.encode())
			self.scheduled = True
