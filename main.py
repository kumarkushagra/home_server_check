import os
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

HOME_SERVER_URL = os.getenv("HOME_SERVER_URL")
if not HOME_SERVER_URL:
    raise Exception("HOME_SERVER_URL not set in .env")  # Ensure .env contains this variable!

app = FastAPI()

class URLRequest(BaseModel):
    imageUrl: str

@app.post("/sendURL")
def send_url(data: URLRequest):
    try:
        response = requests.post(HOME_SERVER_URL, json={"imageUrl": data.imageUrl})
        response.raise_for_status()  
        
        return response.json() 

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, port=8000, reload=True)
