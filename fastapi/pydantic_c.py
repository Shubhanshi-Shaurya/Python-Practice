from fastapi import FastAPI
import json 
from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator,computed_field
from typing import List,Dict,Optional,Annotated

app=FastAPI()

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title="Name of the patient",description="give the name of patient",examples=['rimjhim'])]
    age:int=Field(gt=0,lt=120)
    email:EmailStr
    weight:float
    height:float=Field(gt=0)
    married:Optional[bool]=None
    allergies:List[str]
    contact:Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icici.com']
        domain_name=value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("not a valid domain")
        return value

    @model_validator(mode='after')
    def validate_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact:
            raise ValueError("Patients older than 60 must have emergency contact")
        return model

    @computed_field
    @property
    def bmi(self)-> float:
        bmi=self.weight/(self.height**2)
        return bmi
        


patient_info={'name':'rimjhim','age':20,'weight':55.5,"height":167.0,"married":False,"allergies":['pollen','dust'],"contact":{'email':'abc@gmail.com','phone':'12345'}}

patient1=Patient(**patient_info)

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')

insert_patient_data(patient1)

# serialization
temp=patient1.model_dump(include=['name','age'])
temp2=patient1.model_dump_json()

print(temp)
