# Bring in lightweight dependencies
from fastapi import FastAPI,  Request, Form
import pickle
import preprocess as ps 
import pandas as pd
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

with open('pipe.pkl', 'rb') as f: 
    model = pickle.load(f)
with open('encoder.pkl', 'rb') as f: 
    encoder = pickle.load(f)  
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/" )

def index(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})
@app.post('/predict')
async def prediction(request: Request, text:str = Form(...)): 
    pred = model.predict([text])
    prediction = encoder.inverse_transform(pred)[0]
    
    return templates.TemplateResponse("index.html", {"request": request, 'data': prediction })   


if __name__ == '__main__':
    uvicorn.run(app)