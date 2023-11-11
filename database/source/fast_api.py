from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import database_functions as db_mngmt


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


@app.post("/return_pieces/")
def return_sum(input: User_input):
    db_mg = (
        db_mngmt.database_manager()
    )  # Class cannot be called outside this function because SQLite3 does not support the multi-threading brought by Fastapi
    pieces_dico = db_mg.get_all_records()
    dico_length = len(pieces_dico)
    json_object = {"res_length_max": dico_length, "res": pieces_dico}
    return json_object
