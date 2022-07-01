from models.base_record import BaseRecord
from typing import Optional


""" list of test attendees """
class Attendee(BaseRecord):
	partner_id: int
	customer_id: int
	email: str = ""
	identifier: Optional[str] = ""
	token: str
