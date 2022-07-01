from typing import List
from fastapi import APIRouter

#models
from ..models.perm import Perm
from models.id_only import IdOnly

# base application classes
from modules.helpers import Helpers

h = Helpers()

router = APIRouter(prefix="/api/v1/perms", tags=["perms"])

@router.get("/", response_model=List[Perm])
async def read_perms():
	return h.listing_endpoint("perms")

@router.post("/", response_model=List[int])
async def create_perms(records: List[Perm]):
	retval = h.adding_endpoint("perms", records)
	return retval

@router.delete("/", response_model=List[int])
async def delete_perms(ids: List[int]):
	retval = h.deleting_endpoint("perms", ids)
	return retval
