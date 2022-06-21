from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/getData")
async def root():
    return {"message": "Lidhen bashk"}
