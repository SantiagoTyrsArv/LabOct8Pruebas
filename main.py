from fastapi import fastapi

app = FastAPI()
@app.get("/")
def read_root():
    return {"status":"ok","message":"API funcionando"}