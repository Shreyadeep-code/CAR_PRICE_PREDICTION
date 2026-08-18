from fastapi import FastAPI
from schema.user_input import UserInput
from model.predict import predict_output
from fastapi.responses import JSONResponse

app=FastAPI()

@app.get('/')
def Home():
    return {"message : welcome for car price prediction"}

@app.post('/predict')
def Predict(data :UserInput):
    inputdf={
        'name':data.name,
        'company':data.company,
        'year':data.year,
        'kms_driven':data.kms_driven,
        'fuel_type':data.fuel_type
    }
    try:
        price=predict_output(inputdf)['Price Of Car ']
        return JSONResponse(status_code=200,content={'Price of Car' : price})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))

   

