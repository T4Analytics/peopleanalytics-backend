from typing import List
from fastapi import APIRouter

#models
from models.user import User
from models.id_only import IdOnly

# base application classes
from modules.helpers import Helpers

h = Helpers()

router = APIRouter(prefix="/api/v1/users", tags=["users"])

@router.get("/", response_model=List[User])
async def read_users():
	customer_ids = h.field2tuple(h.db_select("customers", {"parent_id":0}))
	return h.listing_endpoint("users", additional_conds={"customer_id__in":customer_ids})

@router.post("/", response_model=List[int])
async def create_users(records: List[User]):
	retval = h.adding_endpoint("users", records, additional_fields={"customer_id":0})
	return retval

@router.delete("/", response_model=List[int])
async def delete_users(ids: List[int]):
	retval = h.deleting_endpoint("users", ids)
	return retval
