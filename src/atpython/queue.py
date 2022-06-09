import datetime
import subprocess
import atpython
def queue() -> list[atpython.job.Job]:
	atq = subprocess.run(
			('atq'),
			encoding = 'utf-8',
			stdout = subprocess.PIPE) \
		.stdout \
		.split('\n')
	jobs = []
	for line in [l for l in atq if l != ""]:
		data = line.split()
		number = int(data[0])
		at = datetime.datetime.strptime(
			' '.join(data[1:6]),
			'%a %b %d %H:%M:%S %Y')
		command = subprocess.run(
				('at', '-c', str(number)),
				encoding = 'utf-8',
				stdout = subprocess.PIPE) \
			.stdout \
			.split('\n')[-2]
		jobs.append(atpython.job.Job(
				number = number,
				command = command,
				at = at))
	return jobs
