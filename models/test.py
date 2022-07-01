from models.base_record import BaseRecord
from modules.enums import TestType


""" tests created by t4 """
class Test (BaseRecord):
	typ: TestType
	title: str
