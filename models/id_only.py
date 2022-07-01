from pydantic import BaseModel
from models.base_record import BaseRecord

""" user groups """
class IdOnly(BaseModel):
	id: int
