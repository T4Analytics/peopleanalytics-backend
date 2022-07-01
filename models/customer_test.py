from models.base_record import BaseRecord

""" tests created by our partners (eg peoplise) for their customers (eg turkcell) """
class CustomerTest(BaseRecord):
	partner_id: int
	customer_id: int
	test_id: int
	pretext: str
	title: str
	posttext: str
	timelimit_sec: int
