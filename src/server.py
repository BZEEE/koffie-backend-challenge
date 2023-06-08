from fastapi import FastAPI
from .routes.vin_routes import vin_routes
from .routes.database_routes import database_routes

# create the main app server
app = FastAPI()
# add various routes as needed
app.include_router(vin_routes)
app.include_router(database_routes)
