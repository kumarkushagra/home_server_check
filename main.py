from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
async def root():
    def fetch_data(url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return "online"  # Assuming the response is in JSON format
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return "offline"
    return fetch_data("ssh.devvdeploy.site")

if __name__=="__main__":
    uvicorn.run(app, port=8000)