from typing import List
from pydantic import Json
from models.base_record import BaseRecord


""" list of options (choices) in each question """
class OptionGroup(BaseRecord):
	texts: Json[List[str]]
	images: Json[List[str]]
