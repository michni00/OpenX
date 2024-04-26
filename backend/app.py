import uuid
from fastapi import FastAPI, Body
from pydantic import BaseModel
from backend.methods import fahrenheit_to_celsius
from backend.methods_ai import fahrenheit_to_celsius_ai
app = FastAPI()

def generate_app_id():
    app.state.app_id = str(uuid.uuid4())

class TemperatureIn(BaseModel):
    fahrenheit: float
    
class TemperatureOut(BaseModel):
    celsius: float
    app_id: str


@app.on_event("startup")
async def startup_event():
    generate_app_id()

@app.get("/")
def home():
    return {"everything is": "OK"}

@app.post("/convert", response_model=TemperatureOut)
async def convert_temperature(temp: TemperatureIn = Body(...)):
    fahrenheit = temp.fahrenheit
    return {"celsius": fahrenheit_to_celsius(fahrenheit), 
            "app_id": app.state.app_id}
    
@app.post("/convert_ai", response_model=TemperatureOut)
async def convert_temperature(temp: TemperatureIn = Body(...)):
    fahrenheit = temp.fahrenheit
    return {"celsius": fahrenheit_to_celsius_ai(fahrenheit), 
            "app_id": app.state.app_id}