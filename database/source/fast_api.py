from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class User_input(BaseModel):
    ip1: str
    ip2: str
    ip3: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/return_sum")
def return_sum(input: User_input):
    print(input.ip2)
    res = input.ip3
    json_object = {
        "res_length": 0,
        "Author": input.ip1,
        "Creation_date": input.ip2,
        "Lost_date": input.ip3,
    }
    # with open("volume/res.json", "w") as outfile:
    # outfile.write(json_object)
    return json_object
