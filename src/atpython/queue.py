from pathlib import Path
from datetime import datetime
from subprocess import PIPE, run
from atpython import Job
def get_queue() -> list[Job]:
	cmd_queue = run(('atq'), encoding = 'utf-8', stdout = PIPE)
	jobs = []
	for line in [l for l in cmd_queue.stdout.split('\n') if l != ""]:
		data = line.split()
		number = int(data[0])
		raw = str(' '.join(data[1:6]))
		at = datetime.strptime(raw, '%a %b %d %H:%M:%S %Y')
		raw = run(('at', '-c', str(number)), stdout = PIPE).stdout
		command = raw \
			.decode() \
			.split('\n')[-2]
		j = Job(command, at)
		j.number = number
		j.raw = raw
		j.scheduled = True
		jobs.append(j)
	return jobs
