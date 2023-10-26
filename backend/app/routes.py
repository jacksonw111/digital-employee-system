from fastapi import APIRouter

from app import customer


api_router = APIRouter()
api_router.include_router(customer.routes.api_router)
