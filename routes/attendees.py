import pprint
from typing import List
from fastapi import APIRouter

#models
from models.attendee import Attendee

# base application classes
from modules.helpers import Helpers

h = Helpers()

router = APIRouter(prefix="/api/v1/attendees", tags=["attendees"])

@router.get("/")
async def read_attendees():
	customers = h.db_select("customers", {"parent_id__gt":0})
	customer_ids = h.field2tuple(customers)
	customers = dict(h.field2key(customers))
	data = h.db_select("attendees", conds={"customer_id__in":customer_ids, "is_deleted":0})
	for idx in range(len(data)):
		data[idx] = dict(data[idx])
		data[idx]["customer"] = dict(customers[data[idx]["customer_id"]])
	return data

@router.post("/", response_model=List[int])
async def create_attendees(records: List[Attendee]):
	retval = h.adding_endpoint("attendees", records)
	return retval

@router.delete("/", response_model=List[int])
async def delete_attendees(ids: List[int]):
	retval = h.deleting_endpoint("attendees", ids)
	return retval
