from fastapi import FastAPI 
from pydantic import BaseModel, EmailStr , Field
from datetime import date

app = FastAPI()



class Order(BaseModel) :
    order_id : str
    order_date : date
    order_value : int 
    user_email : str 


class UserValidation(BaseModel):
    name : str = Field(min_length= 5 )
    age : int = Field(gt= 10 , lt=120)
    email : EmailStr 
    password : str = Field(min_length=8)




class User : 
    name : str 
    age : int 
    email : str 
    password : str 
    orders : list[Order]

    def __init__(self , name , age , email , password ):
        self.name = name 
        self.age = age 
        self.email = email
        self.password = password


users = []

@app.post('/add/users')
async def getData(data : UserValidation) :
    user = User(**data.model_dump())
    users.append(user)

    return {
        'message'  : "works well ",
        'users'  : users
        
    }

async def getData() :
    return {
        'message' : "this is the get method "
    }

