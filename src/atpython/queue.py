from pathlib import Path
from datetime import datetime
from subprocess import PIPE, run
from atpython import Job
class Queue(object):
	FORMAT_DATE = '%a %b %d %H:%M:%S %Y'
	def __init__(self):
		self.jobs = self._get_jobs()
	def _get_jobs(self) -> list[Job]:
		r = run(('atq'), encoding = 'utf-8', stdout = PIPE)
		jobs = []
		for line in [l for l in r.stdout.split('\n') if l != ""]:
			data = line.split()
			number = int(data[0])
			raw = str(' '.join(data[1:6]))
			d = datetime.strptime(raw, Queue.FORMAT_DATE)
			j = Job("", d)
			j.number = number
			jobs.append(j)
		return jobs
