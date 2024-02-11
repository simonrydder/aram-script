from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def start_game() -> str:
    return 'Game Started'