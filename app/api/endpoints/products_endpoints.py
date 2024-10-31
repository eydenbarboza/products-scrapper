from enum import Enum
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, Query
from fastapi.encoders import jsonable_encoder

from app.domain.services.product_service import get_service

router = APIRouter()

@router.post("/products-required")
async def required_get_products(
    url: str = Query(...)
    ):
    """ Endpoint required to obtain products. """
    try:
        service = get_service()
        data = await service.get_products(
            url=url
        )
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


@router.get("/products-proposal")
async def proposed_get_products(
    url: str = Query(...), 
    limit: int = Query(15)
    ):
    """ Proposed endpoint to obtain products. """
    try:
        service = get_service()
        data = await service.get_products(
            url=url,
            limit=limit
        )
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))