import uvicorn
from fastapi import (
    APIRouter,
    FastAPI,
    Request,
    status,
)
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, RedirectResponse

from pkg_15903.configs.logger import LOGGING_CONFIG
from pkg_15903.routers import api, info, versions


app = FastAPI()
router = APIRouter()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    content = {"Error": f"Invalid data - {exc.errors()[0]['msg']}"},

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=content[0]
    )


@app.get("/")
def home():
    return RedirectResponse(url='/versions')


@app.get("/health")
def get_status():
    return {"status": "ok"}


app.include_router(info.router)
app.include_router(versions.router)
app.include_router(api.router)


if __name__ == '__main__':  # pragma: no cover
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        workers=4,
        forwarded_allow_ips='*',
        log_level="debug",
        log_config=LOGGING_CONFIG
    )
