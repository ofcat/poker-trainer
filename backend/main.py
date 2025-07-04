from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() 

##https://youtu.be/YIF2RVgqqlk?feature=shared

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev only
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/api/hello')
def say_hello():
    return {"message: Hello"}