from fastapi import FastAPI
from pydantic import BaseModel

# FASTAPI app:
app = FastAPI(description="Api for testing")
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/", )

def get_app():
    return app