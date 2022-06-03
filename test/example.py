from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]
	/ 'src'))
from datetime import datetime, timedelta
from atpython import Job
def main():
	Job('touch ~/dev/atpython/ayylmao', datetime.now() + timedelta(seconds = 5)).schedule()
if __name__ == '__main__':
	main()
