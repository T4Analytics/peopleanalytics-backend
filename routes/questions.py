from typing import List
from fastapi import APIRouter

#models
from models.question import Question
from models.id_only import IdOnly

# base application classes
from modules.helpers import Helpers

h = Helpers()

router = APIRouter(prefix="/api/v1/questions", tags=["questions"])

@router.get("/", response_model=List[Question])
async def read_questions():
	return h.listing_endpoint("questions")

@router.post("/", response_model=List[int])
async def create_questions(records: List[Question]):
	retval = h.adding_endpoint("questions", records)
	return retval

@router.delete("/", response_model=List[int])
async def delete_questions(ids:List[int]):
	retval = h.deleting_endpoint("questions", ids)
	return retval
