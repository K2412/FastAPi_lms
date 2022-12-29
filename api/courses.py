import fastapi
from pydantic import BaseModel
from typing import Optional, List
#router for app(similar to blue print in Flask)
router = fastapi.APIRouter()


@router.get("/courses")
async def read_course():
    return {"courses": []}



@router.post("/courses")
async def create_courses():
    return {"courses": []}


@router.get("/courses/:id")
async def read_course():
    return {"courses": []}


@router.patch("/courses/:id")
async def update_course():
    return {"courses": []}


@router.delete("/courses/:id")
async def delete_users():
    return {"courses": []}


@router.get("/courses/:id/sections")
async def read_course_sections():
    return {"courses": []}