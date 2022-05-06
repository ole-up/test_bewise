import os

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.questions.api import router


app = FastAPI(
    title="Questions API",
    version="0.0.1"
)

app.include_router(router)


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
