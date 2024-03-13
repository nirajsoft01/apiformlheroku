from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    Response: str

# Load the saved model
model = pickle.load(open('sbmodel.sav', 'rb'))

@app.post('/generate_summary')
def generate_summary(input_data: InputData):
    input_text = input_data.Response
    generated_summary = model.predict(input_text)
    return {'generated_summary': generated_summary}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
