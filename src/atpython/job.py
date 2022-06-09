import datetime
import subprocess
import atpython
class Job(object):
	def __init__(	self,
			command: str,
			at: datetime.datetime,
			scheduled: bool = False,
			number: int = -1,
			raw: bytes = None):
		self.command = command
		self.at = at
		self.scheduled = scheduled
		self.number = number
		self.raw = raw
	def schedule(self):
		if not self.scheduled:
			cmd = self.command
			t = self.at.strftime('%Y%m%d%H%M.%S')
			subprocess.run(
				('at', '-t', t.encode()),
				input = cmd.encode())
			print(self)
			self = max(
				atpython.queue.queue(),
				key = lambda j: j.number)
			print(self)
