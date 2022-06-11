#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]
	/ 'src'))
from datetime import datetime, timedelta
from atpython import *
def main():
	j = Job(b"ayylmao", datetime.now(), b"thesearesomebytes", 'a', "sbondoc")
	print(j.command)
	print(j.at)
	print(j.raw)
	print(j.queue)
	print(j.user)
	jobs = job_queue()
	for (number, j) in jobs.items():
		print(number, j.command, j.at, j.queue, j.user)
	schedule(b"touch ~/dev/atpython/ayylmao", datetime.now() + timedelta(weeks = 1))
	return
if __name__ == '__main__':
	main()
