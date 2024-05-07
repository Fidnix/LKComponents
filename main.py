from fastapi import FastAPI, Form
from typing import Annotated

app = FastAPI()

@app.post("/")
async def root(descripcion_tardanza: Annotated[str, Form()]):
    return {"desc": descripcion_tardanza}
    