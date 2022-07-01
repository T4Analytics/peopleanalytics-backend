from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

# class Action(SQLModel, table=True):

class Config(SQLModel.Config):
	arbitrary_types_allowed = True

""" base record type """
# class BaseRecord(BaseModel):
class BaseRecord(SQLModel, table=True, config=Config):
	id: Optional[int] = Field(default=None, primary_key=True)
	is_deleted: Optional[int] = 0
	created_at: Optional[datetime]
	updated_at: Optional[datetime]
