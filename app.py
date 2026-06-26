from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "hello pls this is my last chance"
