from typing import List
from fastapi import APIRouter

#models
from models.customer import Customer

# base application classes
from modules.helpers import Helpers

h = Helpers()

router = APIRouter(prefix="/api/v1/customers", tags=["customers"])

@router.get("/", response_model=List[Customer])
async def read_customers():
	return h.listing_endpoint("customers", additional_conds={"parent_id__gt":0, "is_deleted":0})

@router.post("/", response_model=List[int])
async def create_customers(records: List[Customer]):
	retval = h.adding_endpoint("customers", records, additional_fields={"parent_id":0})
	return retval

@router.delete("/", response_model=List[int])
async def delete_customers(ids: List[int]):
	retval = h.deleting_endpoint("customers", ids)
	return retval
