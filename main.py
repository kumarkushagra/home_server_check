from fastapi import FastAPI
import requests

app = FastAPI()

def fetch_data(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return "online"
    except requests.exceptions.RequestException:
        return "offline"

@app.get("/")
async def root():
    return fetch_data("https://ssh.devvdeploy.site")

if __name__=="__main__":
    uvicorn.run(app, port=8000)