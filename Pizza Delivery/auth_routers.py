from fastapi import APIRouter

auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

@auth_router.get('/')
async def home():
    return {'message' : 'Auth router home page'}
    