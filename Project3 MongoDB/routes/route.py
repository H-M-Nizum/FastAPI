# step 5:
from fastapi import APIRouter, HTTPException
from config.database import collection_name
from models.model import EmployeeModel
from schemas.schema import list_serializer, individual_serializer
from bson import ObjectId

router = APIRouter()

#GET Request Method
@router.get('/')
async def get_all_employees():
    employees = list_serializer(collection_name.find())
    return employees


#GET Request Method for specific employee
@router.get('/{id}')
async def get_employee_by_id(id: str):
    employee = collection_name.find_one({"_id": ObjectId(id)})
    if employee:
        return individual_serializer(employee)
    else:
        raise HTTPException(status_code=404, detail="Employee not found")


# # POST Request Method
# @router.post('/')
# async def create_employee(employee : EmployeeModel):
#     collection_name.insert_one(dict(employee))
# POST Request Method
@router.post('/')
async def create_employee(employee: EmployeeModel):
    # Convert the employee model to a dictionary and insert it into the collection
    employee_dict = employee.dict()  # Use the appropriate method to convert to a dict
    data = collection_name.insert_one(employee_dict)

    # Fetch the newly created employee document from the database
    new_employee = collection_name.find_one({"_id": data.inserted_id})

    # Return the serialized employee data
    return individual_serializer(new_employee)


# PUT Request Method
@router.put('/{id}')
async def update_employee(id : str, employee : EmployeeModel):
    updated_employee = collection_name.find_one_and_update({"_id" : ObjectId(id)}, {"$set" : employee.dict()})
    # Check if the employee was found and updated
    if not updated_employee:
        raise HTTPException(status_code=404, detail="Employee Not Found")

    # Return the serialized updated employee data
    return individual_serializer(updated_employee)
    
    
# DELETE Request Method
@router.delete('/{id}')
async def delete_employe(id : str):
    # Attempt to delete the employee from the database
    result = collection_name.delete_one({"_id": ObjectId(id)})

    # Check if any document was deleted
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Employee Not Found")

    # Optionally, you can return a success message or status code
    return {"detail": "Employee deleted successfully"}