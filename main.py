from fastapi import FastAPI
from pydantic import BaseModel, Field#
from typing import Annotated # Using annotated
from datetime import date # To enforce correct date types

app = FastAPI()

assignments:list[str] = [] #Pydantic would parse to and from JSON - objects as strings


# Base Assignment model
# Extend the fields to include custom format field to match mm-dd-yyy
class Assignment(BaseModel):
    #fields:
    id : Annotated[int, "Assignment ID"] # id is infered at object instantiation/creation time
    title: str = Field(title="Assignment title", min_length=2, max_length=50, description="Title must be greater than and less than 2 and 5 characters respectively",default=f"Assignment") # Personally allowing flexibility in title naming
    due_date: Annotated[date, Field(title = "Assignment due date (YYYY-MM-DD)", description="Due date. Format is: YYYY-MM-DD")] # Default date setting is now - when ever you create it
    done: Annotated[bool, "True or False", Field(default=False, description="Must be a boolean")] # simple boolean - set to false as default



# View all assignments
@app.get("/assignments", status_code=200)
def get_assignments():
    """This function returns all assignments in the list of assignment objects"""
    return assignments



# View one assignment - requires knowledge about which particular assignment
# Hence an id passed as a query parameter
@app.get("/assignments/{id}", status_code=200) # passed assignment id as a parameter in the url and status code set as 200 to ensure proper validation
def get_assignment(id: int): # id must be int
    """This function returns a single assignment object based on what was passed as a param"""
    try:
        return assignments[id]
    except ReferenceError as e:
        print(f"Assignment not found.\n{e}")
        return {"error": "Assignment not found"}
    except IndexError as e:
        return {"error": "Index of ID is out of range"}



# Create assignments -> POST /create
@app.post("/create", status_code=201)
def create_assignment(payload: Assignment):
    """This function creates an assignment and saves to a list of assignment objects (json)"""
    try:
        assignment = payload.model_dump() # dictionary representation of object/model
        assignment["id"] = len(assignments)
        assignments.append(assignment)
        print("Assigment created successfully!")
        return {"item": assignment, "status": "successful!"}
    except Exception as e:
        return {"error": "Could not create entry"}
    


# Delete one specific assignment object
@app.delete("/assignments/{id}")
def delete_assignment(id: int):
    """This function deletes one specific assignment from the list of assignment objects"""
    try:
        #Find id first
        for id in assignments: 
            if assignments == None:
                return {"error": "There are no assignments"}
            if assignments[id] == id:
                assignment = assignments[id]
                assignments.pop(id)
                return assignment 
            

    except ReferenceError as e:
        return {"error": f"Assignment not found.\n{e}"}