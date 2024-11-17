from pydantic import BaseModel, Field
from typing import Optional

class SignUpSchema(BaseModel):
    username : str
    email : str
    password : str
    is_active: Optional[bool] = Field(default=True)
    is_staff : Optional[bool] = Field(default=False)
    is_admin : Optional[bool] = Field(default=False)
    
    class config:
        orm_mode = True
        schema_ertra = {
            'example' : {
                'username' : 'Nizum',
                'email' : 'nizum@gmail.com',
                'password' : 'password123',
                'is_active' : True,
                'is_admin' : False,
                'is_staff' : False
            }
        }
