# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Configure CORS settings
origins = [
    "http://localhost",
    "http://localhost:5173",  # Your React app's development server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"message": "Hello, World! from gittyyyyyy"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
