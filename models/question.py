from models.base_record import BaseRecord
from modules.enums import QuestionType
from models.optiongroup import OptionGroup
from sqlmodel import Enum, Column, Field

""" each question in each test """
class Question(BaseRecord):
	typ: QuestionType = Field(sa_column=Column(Enum(QuestionType)))
	pretext: str
	body: str
	posttext: str
	optiongroup_id: OptionGroup # = Field(sa_column=Column(Enum(OptionGroup)))
	# optiongroup_id: Enum[OptionGroup]
	test_id: int
	qorder: int
	# impact: Json
