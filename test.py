from time import time
from fastapi import FastAPI, __version__
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/ping')
async def hello():
    return JSONResponse(
        content={'res': 'pong', 'version': __version__, "time": time()},
        headers={'Content-Type': 'application/json'}
    )