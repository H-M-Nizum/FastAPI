from fastapi import APIRouter

order_router = APIRouter(
    prefix='/order',
    tags=["Order"]
)

@order_router.get('/')
async def home():
    return {'message' : 'This is order home page'}