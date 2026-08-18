import pickle
import pandas as pd

with open('model/car_price_detect.pkl','rb') as f:
    model=pickle.load(f)

def predict_output(user_input:dict):
    df=pd.DataFrame([user_input])

    result=model.predict(df)[0]

    return {
        'Price Of Car ': result
    }
    