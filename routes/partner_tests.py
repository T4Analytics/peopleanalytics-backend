from typing import List
from fastapi import APIRouter

#models
from models.partner_test import PartnerTest
from models.id_only import IdOnly

# base application classes
from modules.helpers import Helpers

h = Helpers()

router = APIRouter(prefix="/api/v1/partner_tests", tags=["partner_tests"])

@router.get("/", response_model=List[PartnerTest])
async def read_partner_tests():
	return h.listing_endpoint("partner_tests")

@router.post("/", response_model=List[int])
async def create_partner_tests(records: List[PartnerTest]):
	retval = h.adding_endpoint("partner_tests", records)
	return retval

@router.delete("/", response_model=List[int])
async def delete_partner_tests(ids: List[int]):
	retval = h.deleting_endpoint("partner_tests", ids)
	return retval
