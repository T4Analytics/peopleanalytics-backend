from models.base_record import BaseRecord


""" each answer from the user """
class Choice(BaseRecord):
	attendee_id: int
	test_id: int
	session_id: int
	question_id: int
	choice: str
	completed_ms: int # how long did it take
