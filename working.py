from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel
import pyrebase

app = FastAPI()

#defining database configurations
firebaseConfig = {"apiKey": "AIzaSyBCpA-tQwpAb3W0Wseq3IoooNGs5y8UaEg",
                  "authDomain": "fir-course-56391.firebaseapp.com",
                  "databaseURL": "https://fir-course-56391-default-rtdb.firebaseio.com/",
                  "projectId": "fir-course-56391",
                  "storageBucket": "fir-course-56391.appspot.com",
                  "messagingSenderId": "581497302237",
                  "appId": "1:581497302237:web:cf339dd7e9d25f6fb5bf34",
                  "measurementId": "G-M322JGF25H"}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

#sample classes of pet
class Pet(BaseModel):
    pet_name: str
    owner_name: str
    pet_age: int
    pet_type: str
    pet_gender: str


class UpdatePet(BaseModel):
    pet_name: Optional[str] = None
    owner_name: Optional[int] = None
    pet_age: Optional[str] = None
    pet_type: Optional[str] = None
    pet_gender: Optional[str] = None


pet_dict = {}

#CREATE_pet_data
@app.post("/create-Pet")
def create_Pet(id: int, Pet: Pet):
    pet_dict = dict()

    pet_dict = {"pet_name": Pet.pet_name, " owner_name": Pet.owner_name,
                "pet_age": Pet.pet_age, "pet_type": Pet.pet_type, "pet_gender": Pet.pet_gender}
    res = db.child("pet").child(f"{id}").set(pet_dict)
    return {"created pet successfully"}, res

#VIEW_pet_data
@app.get("/get-Pet")
def get_Pet(id: int):
    pet_dict = dict()
    res = dict(db.child("pet").child(f"{id}").get().val())
    return res

#UPDATE_pet_data
@app.put("/update-Pet")
def update_Pet(id: int, key: str, val: str):
    pet_dict = dict()
    res = dict(db.child("pet").child(f"{id}").update({key: val}))
    return {"Update successful."}, res

#REMOVE_pet_data
@app.delete("/delete-Pet")
def delete_Pet(Pet_id: int = Query(..., description="The ID of the Pet to delete")):

    db.child("pet").child(f"{Pet_id}").remove()
    return {"Success Pet deleted"}
