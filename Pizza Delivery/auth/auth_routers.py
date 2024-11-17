from fastapi import APIRouter, status, Depends
from .models import UsersModel
from .schemas import SignUpSchema
from database import SessionLocal
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash

auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

# Dependency to get the session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@auth_router.get('/')
async def home():
    return {'message': 'Auth router home page'}

@auth_router.post('/signup')
async def signup(user: SignUpSchema, db: SessionLocal = Depends(get_db)):
    # Check if email already exists
    user_email = db.query(UsersModel).filter(UsersModel.email == user.email).first()
    if user_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User already created using this email.'
        )
        
    # Check if username already exists
    user_username = db.query(UsersModel).filter(UsersModel.username == user.username).first()
    if user_username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User already created using this username.'
        )
    
    # Create new user
    new_user = UsersModel(
        email=user.email,
        username=user.username,
        password=generate_password_hash(user.password),
        is_staff=user.is_staff,
        is_active=user.is_active,
        is_admin=user.is_admin
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
