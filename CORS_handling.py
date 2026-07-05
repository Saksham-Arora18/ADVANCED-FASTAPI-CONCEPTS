from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings

app = FastAPI()



#Allowed Origins(Front-end URl)
origins = settings.origins


app.add_middleware(
    CORSMiddleware,
    allow_origins = origins, #allowed FE
    allow_credentials = True,
    allow_methods = ["*"], #GET,PUT,POST,DELETE
    allow_headers=["*"]
)

@app.get("/")
def home():
    return{
        "message":"CORS ENABLE API"
    }
