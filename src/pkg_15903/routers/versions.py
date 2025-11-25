from fastapi import APIRouter, __version__ as fastapi_version

from pkg_15903 import __version__ as app_version


router = APIRouter(
    prefix="/versions",
    tags=["versions"]
)


@router.get("/")
def get_versions():
    return {
        "versions": {
            "apitest": app_version,
            "fastapi": fastapi_version,
        }
    }
