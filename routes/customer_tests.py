from typing import List
from fastapi import APIRouter

#models
from models.customer_test import CustomerTest
from models.id_only import IdOnly

# base application classes
from modules.helpers import Helpers

h = Helpers()

router = APIRouter(prefix="/api/v1/customer_tests", tags=["customer_tests"])

@router.get("/", response_model=List[CustomerTest])
async def read_customer_tests():
	return h.listing_endpoint("customer_tests")

@router.post("/", response_model=List[int])
async def create_customer_tests(records: List[CustomerTest]):
	retval = h.adding_endpoint("customer_tests", records)
	return retval

@router.delete("/", response_model=List[int])
async def delete_customer_tests(ids: List[int]):
	retval = h.deleting_endpoint("customer_tests", ids)
	return retval
