from fastapi import FastAPI

from pings.view import router as view_router
app = FastAPI()

app.include_router(view_router)


@app.get('/')
def index():
    return {
        "message": "it works"
    }