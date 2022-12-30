from fastapi import FastAPI

from api import user,sections,courses

from app_db.db_setup import engine
from app_db.models import user_models, courses_models

user_models.Base.metadata.create_all(bind=engine)
courses_models.Base.metadata.create_all(bind=engine)



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
