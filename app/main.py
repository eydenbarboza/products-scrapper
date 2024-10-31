import os

from fastapi import FastAPI,Depends
from pymongo import MongoClient
from fastapi.encoders import jsonable_encoder

from api.endpoints import products_endpoints


app = FastAPI()
app.include_router(products_endpoints.router, prefix="/products", tags=["products"])


