from models.base_record import BaseRecord
from typing import Optional


""" list of customers """
class Customer(BaseRecord):
	parent_id: Optional[int] = 0
	title: str = ""
	contact: str = ""
