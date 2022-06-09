from pathlib import Path
from datetime import datetime
from subprocess import PIPE, run
from atpython.job import Job
from atpython.util import queue_dict
def get_queue() -> list[Job]:
	jobs = []
	for j in queue_dict():
		jobs.append(Job(**j))
	return jobs
