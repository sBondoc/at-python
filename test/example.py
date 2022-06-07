from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]
	/ 'src'))
from datetime import datetime, timedelta
from atpython import Job
def main():
	j = Job('touch ~/dev/atpython/ayylmao', datetime.now() + timedelta(minutes = 1))
	print(j.command)
	print(j.at)
	j.schedule()
	return
if __name__ == '__main__':
	main()
