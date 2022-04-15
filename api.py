"""Api file to store api routes."""

from fastapi import FastAPI, status, Query
from fastapi.responses import JSONResponse

import pokemon_functions

OAPI_TAGS = [
    {
        "name": "hello-world",
        "description": "Respond with 'Hello World'."
    },
    {
        "name": "pokemon",
        "description": "Return pokemon info within the pokemon name"
    },
]

app = FastAPI(title="Pokemon API",
              description="Return Pokemon data",
              docs_url="/",
              openapi_tags=OAPI_TAGS)


## Endpoints

@app.get("/hello-world", tags=["hello-world"])
async def hello_world():
    """Return hello world text."""
    return JSONResponse(status_code=status.HTTP_200_OK, content={'msg': 'Hello World!'})


@app.get("/pokemon", tags=["pokemon"])
async def get_pokemon(pokemon_name: str = Query(...)):
    """Return the pokemon data."""
    response = pokemon_functions.get_pokemon_data(pokemon_name)
    return JSONResponse(status_code=response['status_code'], content=response)
