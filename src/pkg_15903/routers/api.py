import validators
from fastapi import APIRouter
from fastapi.exceptions import RequestValidationError

from pkg_15903.core.cls_requests import ClsRequests


router = APIRouter(
    prefix="/api",
    tags=["api"]
)


@router.post("/")
async def run_app(data: dict):
    url = data.get('url')
    if url is not None:
        if all([url.startswith('http'), validators.url(url)]):
            start = ClsRequests()
            return start.checklinks(url=url)

        else:
            """invalid url address outside of validators check"""
            raise RequestValidationError(
                [{"loc": ["body"], "msg": "Expect data in JSON Key-Value Pair Structure {'url': 'http(s)://xxxx'}", "type": "value_error.url.host"}],
                body={'url': url}
            )
    else:
        """key: url not found OR value: address is None"""
        raise RequestValidationError(
            [{"loc": ["body"], "msg": "Expect data in JSON Key-Value Pair Structure {'url': 'http(s)://xxxx'}", "type": "value_error.missing"}],
            body={}
        )
