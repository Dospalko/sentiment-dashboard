from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Sentiment Analysis API")

# NASTAVENIE CORS - kritické pre komunikáciu s Reactom
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Povoľ origin tvojej React appky
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Tu budeme neskôr pridávať ďalší kód...