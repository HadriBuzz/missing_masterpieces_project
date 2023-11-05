from fastapi import FastAPI
from pydantic import BaseModel


class User_input(BaseModel):
    _id: float
    x: float
    y: float


app = FastAPI()


@app.post("/return_sum")
def return_sum(input: User_input):
    res = input.x + input.y
    json_object = str(res)
    with open("volume/res.json", "w") as outfile:
        outfile.write(json_object)
    return res


@app.post("/get_url_by_id")
def operate(input: User_input):
    res = get_dico_by_id(input._id)
    return res
