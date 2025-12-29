from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root ():
    return {"message" : "Service is running"}

@app.get("/health")
def health():
    return {"status" : "Ok"}

