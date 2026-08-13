from fastapi import FastAPI,HTTPException,Query
import json 
import pydantic

app=FastAPI()

def load_data():
    pass


@app.get("/sort")
def sort_patients(sort_by:str=Query(...,description="Sort on the basis of height, weight or BMI"),order:str=Query('asc',description="sort in asc or desc order")):
    valid_fields=['height','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail="Invalid field")

    if order not in ["asc","desc"]:
        raise HTTPException(status_code=400,detail="Invalid order")

    data=load_data()

    sort_order=True if order=='desc' else False

    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=True)
    
    return sorted_data




    
