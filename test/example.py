#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]
	/ 'src'))
from datetime import datetime, timedelta
from atpython import *
def main():
	j = Job('touch ~/dev/atpython/atpython/ayylmao', datetime.now() + timedelta(weeks = 1))
	print(j.__dict__)
	j.schedule()
	print(j.__dict__)
	for j in get_queue():
		print(j.command, j.at)
	return
	for i in range(5):
		j = Job('touch ~/dev/atpython/ayylmao', datetime.now() + timedelta(weeks = 1, minutes = i + 1))
		j.schedule()
if __name__ == '__main__':
	main()
