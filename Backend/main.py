import os
from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator
from routes import router
from database import client
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
Instrumentator().instrument(app).expose(app)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI To-Do App!"}

@app.get("/healthz")
async def healthz():
    return {"status": "ok", "version": os.getenv("APP_VERSION", "dev")}

@app.get("/readyz")
async def readyz():
    try:
        await client.admin.command("ping")
    except Exception:
        raise HTTPException(status_code=503, detail="database unavailable")
    return {"status": "ready"}
