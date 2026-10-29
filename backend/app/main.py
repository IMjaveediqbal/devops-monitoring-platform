from fastapi import FastAPI

app = FastAPI(
    title="DevOps Monitoring Platform",
    description="A learning project for Docker and DevOps monitoring",
    version="1.0.0",
)


@app.get("/")
def read_root():
    return {
        "message": "DevOps Monitoring Platform API is running!",
        "status": "healthy",
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}