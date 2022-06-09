#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]
	/ 'src'))
from datetime import datetime, timedelta
import atpython.job
def main():
	j = atpython.job.Job('touch ~/dev/atpython/atpython/ayylmao', datetime.now() + timedelta(weeks = 1))
	print(j.__dict__)
	j.schedule()
if __name__ == '__main__':
	main()
