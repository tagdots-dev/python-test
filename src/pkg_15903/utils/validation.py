import pkg_19544
from pydantic import BaseModel, field_validator


class ClsValidate(BaseModel):
    url: str

    @field_validator('url')
    @classmethod
    def chk_url(cls, url: str) -> str:
        if not pkg_19544.evaluate_url(url, allow_http=True):
            raise ValueError()
        return url
