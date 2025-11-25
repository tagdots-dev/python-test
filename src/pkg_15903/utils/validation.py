import validators
from pydantic import BaseModel, field_validator


class ClsValidate(BaseModel):
    url: str

    @field_validator('url')
    @classmethod
    def chk_url(cls, url: str) -> str:
        if not all((
                url.startswith(('http', 'git')),
                validators.url(url))):
            raise ValueError()
        return url
