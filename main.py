from fastapi import FastAPI, Path, Query
# for validation and serialisation
from pydantic import BaseModel
from typing import Optional, List

from api import user,sections,courses

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing courses and students",version="0.0.1",
    contact={
        "name": "Kevin",
        "email": "Kevin@example.com",
    },
    license_info={
        "name": "MIT",
    },
)

app.include_router(user.router)
app.include_router(sections.router)
app.include_router(courses.router)
