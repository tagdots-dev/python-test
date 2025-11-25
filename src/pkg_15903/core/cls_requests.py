from logging import config, getLogger

import requests
from fastapi.routing import HTTPException
from requests import ConnectionError, HTTPError, RequestException

from pkg_15903.configs.constants import HEADER_DEFAULT, LOG_LEVEL, REQUESTS_TIMEOUT
from pkg_15903.configs.logger import LOGGING_CONFIG


"""initialize logging"""
config.dictConfig(LOGGING_CONFIG)
logger = getLogger('default')
logger.setLevel(LOG_LEVEL)


class ClsRequests:
    def __init__(self):
        pass

    def checklinks(self, url):
        try:
            response = requests.get(url, allow_redirects=True, verify=True, headers=HEADER_DEFAULT, timeout=REQUESTS_TIMEOUT)
            response.raise_for_status()
            status = response.status_code
            logger.info(f'url: {url}, status: {status}')
            return {"url": f"{url}", "status": f"{status}"}

        except HTTPError as err:
            status = err.response.status_code
            logger.error(f'url: {url}, status: {status}')
            content = f'{{"Error_Type": "HTTPError", "Status_Code": {status}}}'
            raise HTTPException(status_code=status, detail=content)

        except ConnectionError as err:
            status = 500
            logger.error(f'url: {url}, status: {status}, err: {err}')
            raise HTTPException(status_code=status, detail="Error_Type - ConnectionError")

        except RequestException as err:  # pragma: no cover
            status = 500
            logger.error(f'url: {url}, status: {status}, err: {err}')
            raise HTTPException(status_code=status, detail="Error_Type - RequestException")
