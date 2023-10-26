import uvicorn
from app.main import app  # noqa

if __name__ == "__main__":
    uvicorn.run(
        "dev_server:app",
        host="127.0.0.1",
        port=9090,
        env_file=".env.dev",
        reload=True,
        reload_excludes="*.pyc",
    )
