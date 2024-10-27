# step 3:
from pydantic import BaseModel

class EmployeeModel(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    salary: float