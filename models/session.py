from datetime import datetime
from models.base_record import BaseRecord
from modules.enums import SessionState

""" active sessions """
class Session(BaseRecord):
	attendee_id: str
	test_id: int
	state: SessionState
	started_at: datetime
	finished_at: datetime
	state: SessionState
	token: str
	spent_sec: int
