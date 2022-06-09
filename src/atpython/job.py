from datetime import date, datetime, time
from subprocess import run
from atpython.util import queue_dict
class Job(object):
	def __init__(self, command: str, at: datetime, scheduled: bool = False, number: int = -1, raw: bytes = None, **kwargs):
		self.command = command
		self.at = at
		self.scheduled = scheduled
		self.number = number
		self.raw = raw
	def schedule(self):
		if not self.scheduled:
			cmd = self.command
			t = self.at.strftime('%Y%m%d%H%M.%S')
			run(('at', '-t', t.encode()), input = cmd.encode())
			self.scheduled = True
			self.number = _get_latest()
def _get_latest() -> int:
	return max([j['number'] for j in queue_dict()])
