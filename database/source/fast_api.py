from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class User_input(BaseModel):
    ip1: str
    ip2: str
    ip3: str
    ip4: int


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
    json_object = {
        "res_length_max": input.ip4,
        "res": [
            {
                "name": "Chez Tortoni",
                "author": "Manet",
                "creation_date": 1875,
                "Lost_date": 1990,
                "url": "https://upload.wikimedia.org/wikipedia/commons/b/b4/Édouard_Manet%2C_Chez_Tortoni.jpg",
            },
            {
                "name": "Le Christ dans la tempête sur la mer de Galilée",
                "author": "Rembrandt",
                "creation_date": 1633,
                "lost_date": 1990,
                "url": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Rembrandt_Christ_in_the_Storm_on_the_Lake_of_Galilee.jpg",
            },
            {
                "name": "Le Concert ",
                "author": "Vermeer",
                "creation_date": 1666,
                "lost_date": 1990,
                "url": "https://upload.wikimedia.org/wikipedia/commons/c/c8/Vermeer_The_concert.JPG",
            },
        ],
    }

    return json_object
