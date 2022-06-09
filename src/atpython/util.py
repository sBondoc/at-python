from datetime import datetime
from subprocess import PIPE, run
def queue_dict() -> list[dict]:
	atq = run(('atq'), encoding = 'utf-8', stdout = PIPE) \
		.stdout \
		.split('\n')
	jobs = []
	for line in [l for l in atq if l != ""]:
		data = line.split()
		number = int(data[0])
		at = datetime.strptime(
			' '.join(data[1:6]),
			'%a %b %d %H:%M:%S %Y')
		command = run(('at', '-c', str(number)), encoding = 'utf-8', stdout = PIPE) \
			.stdout \
			.split('\n')[-2]
		jobs.append({
			'number': number,
			'command': command,
			'at': at})
	return jobs
