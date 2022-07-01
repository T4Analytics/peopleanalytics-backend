from datetime import datetime
from typing import Union
from models.base_record import BaseRecord
from pydantic import Json

""" each paper filled by attendees """
class Paper(BaseRecord):
	partner_id: int
	customer_id: int
	test_id: int
	attendee_id: int
	token: str
	started_at: Union[datetime, None] = None
	# started_at: Optional[datetime]
	# finished_at: Optional[datetime]
	# evaluated_at: Optional[datetime]
	# pdf_at: Optional[datetime]
	# result_json: Json
	# spent_sec: int
	# min_start_at: Optional[datetime]
	# max_end_at: Optional[datetime]
