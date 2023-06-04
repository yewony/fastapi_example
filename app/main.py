import os
from asyncio import sleep
from datetime import datetime
from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

SERVER_START_DATE = datetime.now()
try:
    with open('/code/app/build_and_push_date.txt', 'r') as file:
        BUILD_DATE = file.read().strip()
except FileNotFoundError:
    with open('./app/build_and_push_date.txt', 'r') as file:
        BUILD_DATE = file.read().strip()


app = FastAPI(title="test API Docs")


@app.get("/", include_in_schema=False)
async def health_check(request: Request):
    await sleep(0.1)
    return {'message': 'healthy', 'build_date': BUILD_DATE, 'SERVER_START_DATE': f'{datetime.strftime(SERVER_START_DATE, "%Y-%m-%d %H:%M:%S")}'}


@app.get("/hi", include_in_schema=False)
async def get_hi(request: Request):
    await sleep(0.1)
    return 'hi!'



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
