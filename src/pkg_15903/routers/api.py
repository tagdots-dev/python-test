import pkg_19544
from fastapi import APIRouter
from fastapi.exceptions import RequestValidationError

from pkg_15903.core.cls_requests import ClsRequests


router = APIRouter(
    prefix="/api",
    tags=["api"],
)


@router.post("")
async def run_app(data: dict):
    url = data.get('url')
    if url is not None:
        if pkg_19544.evaluate_url(url, allow_http=True):
            req = ClsRequests()
            return req.checklinks(url=url)

        else:
            """invalid url address outside of evaluate_url check"""
            raise RequestValidationError(
                [{"loc": ["body"], "msg": "(1) Expect data in JSON KV Pair Structure {'url': 'http(s)://xxxx'}", "type": "value_error.url.host"}],
                body={'url': url}
            )
    else:
        """key: url not found OR value: address is None"""
        raise RequestValidationError(
            [{"loc": ["body"], "msg": "(2) Expect data in JSON KV Pair Structure {'url': 'http(s)://xxxx'}", "type": "value_error.missing"}],
            body={}
        )
