from fastapi import FastAPI
from root.AppConfig import BASE_APP, HOST, PORT, RELOAD, LOG_LEVEL
import uvicorn

app = FastAPI()


@app.get('/')
async def boot_app():
    return {
        "api_version": 1.0,
        "api_description": "A Rest Microservice for Create Finders FullStack Project",
        "author": "Siddhartha Verma @ CreateFinders-Youtube"
    }


if __name__ == '__main__':
    uvicorn.run(BASE_APP, host=HOST, port=PORT, reload=RELOAD, log_level=LOG_LEVEL)
