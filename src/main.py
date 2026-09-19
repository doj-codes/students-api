from fastapi import FastAPI

import config

app = FastAPI(title="Students-API", version=config.APP_VERSION)


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/students")
def list_students():
    return [{"id": 1, "name": "Ana"}, {"id": 2, "name": "Luis"}]
