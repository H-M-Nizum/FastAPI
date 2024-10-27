# Step 4:
def individual_serializer(employee):
    return {
        "id" : str(employee["_id"]),
        "first_name": employee["first_name"],
        "last_name": employee["last_name"],
        "email": employee["email"],
        "phone_number": employee["phone_number"],
        "salary": employee["salary"]
    }
    
    
def list_serializer(employees):
    return [individual_serializer(employee) for employee in employees]
