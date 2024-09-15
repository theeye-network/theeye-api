from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/test")
def test():
    return JSONResponse(content={"message": "This is a test response"})
