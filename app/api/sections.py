import fastapi
from pydantic import BaseModel
from typing import Optional, List
#router for app(similar to blue print in Flask)
router = fastapi.APIRouter()



@router.get("/section/{id}")
async def read_section():
    return {"courses": []}



@router.get("/section/{id}/content-blocks")
async def read_section_content_blockers():
    return {"courses": []}



@router.get("/content-blocks/{id}")
async def read_containt_blockers():
    return {"courses": []}