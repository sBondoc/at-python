from datetime import datetime
from subprocess import PIPE, run
from atpython.job import Job
def job_queue() -> dict[int, Job]:
	atq = run(('atq'), encoding = 'utf-8', stdout = PIPE).stdout.split('\n')
	jobs = {}
	for line in [l for l in atq if l != ""][1:]:
		data = line.split()
		number = int(data[0])
		at = datetime.strptime(
			' '.join(data[1:6]),
			'%a %b %d %H:%M:%S %Y')
		raw = details(number)
		queue = data[6]
		user = data[7]
		command = raw \
			.decode('utf-8') \
			.split('\n')[-2] \
			.encode('utf-8')
		jobs[number] = Job(command, at, raw, queue, user)
	return jobs
def details(id: int) -> bytes:
	return run(('at', '-c', str(id)), stdout = PIPE).stdout
def schedule(command: bytes, at: datetime):
	run(('at', '-t', at.strftime('%Y%m%d%H%M.%S')), input = command)
