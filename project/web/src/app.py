from fastapi import Request
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from perlin_gener import map_fin
from squares import generate_map
from xoring import generate_xor
from graphic import create_terrain

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")



@app.get("/")
async def home():
    return FileResponse("static/html/div.html")

@app.post("/")
async def create(request: Request):
    data = await request.json()

    type_of = int(data['type_of_generation'])
    n_of_cunks = int(data['chunks'])
    height = int(data['height'])
    length_of_chunk = int(data['length'])

    if type_of == 2:
        create_terrain(map_fin(n_of_cunks, length_of_chunk, height))
    elif type_of == 1:
        create_terrain(generate_xor(n_of_cunks, length_of_chunk, height))
    elif type_of == 3:
        create_terrain(generate_map(n_of_cunks, length_of_chunk, height))





if __name__ == '__main__':
    uvicorn.run('app:app', port=8000, reload=True)