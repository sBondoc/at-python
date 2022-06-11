from datetime import datetime
class Job(object):
	def __init__(self, command: bytes, at: datetime, raw: bytes, queue: str, user: str):
		self._command = command
		self._at = at
		self._raw = raw
		self._queue = queue
		self._user = user
	@property
	def command(self) -> bytes:
		return self._command
	@property
	def at(self) -> datetime:
		return self._at
	@property
	def raw(self) -> bytes:
		return self._raw
	@property
	def queue(self) -> str:
		return self._queue
	@property
	def user(self) -> str:
		return self._user
