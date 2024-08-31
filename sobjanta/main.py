# your_package_name/main.py

from fastapi import FastAPI
from sobjanta.api import app as api_app

app = FastAPI()

# Include the API router
app.include_router(api_app)
