from typing import List
from fastapi import APIRouter

#models
from models.test import Test
from models.id_only import IdOnly

# base application classes
from modules.helpers import Helpers

h = Helpers()

router = APIRouter(prefix="/api/v1/tests", tags=["tests"])

@router.get("/", response_model=List[Test])
async def read_tests():
	return h.listing_endpoint("tests")

@router.post("/", response_model=List[int])
async def create_tests(records: List[Test]):
	retval = h.adding_endpoint("tests", records)
	return retval

@router.delete("/", response_model=List[int])
async def delete_tests(ids: List[int]):
	retval = h.deleting_endpoint("tests", ids)
	return retval
