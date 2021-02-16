from fastapi import FastAPI
from pydantic import BaseModel
import pangu

app = FastAPI()

class Body(BaseModel):
    text: str


@app.post('/api/pangu')
def parse_text(body: Body):
    return pangu.spacing_text(body.text)