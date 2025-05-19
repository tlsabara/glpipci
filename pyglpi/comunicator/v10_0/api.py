import os
from dotenv import load_dotenv
import httpx

from pyglpi.commons.webs import BasicAuth
from pyglpi.comunicator.v10_0.interface_errors import (
    InitSessionError,
    ClientGlpiError401,
    ClientGlpiError400,
    ClientGlpiError404,
    ClientGlpiConfigurationError,
)


class GlpiApiHeadersData:
    load_dotenv()
    _ENV_APP_TOKEN: str = os.getenv('GLPI_APP_TOKEN')
    _ENV_USER_TOKEN: str = os.getenv('GLPI_USER_TOKEN')

    def __init__(self,
                 app_token: str | None = None,
                 user_token: str | None = None,
                 session_token: str | None = None,
                 ):
        self.load_from_env()
        self.app_token = app_token or self._ENV_APP_TOKEN
        self.user_token = user_token or self._ENV_USER_TOKEN
        self.session_token = session_token

        if self.app_token is None and self.user_token is None:
            raise ClientGlpiConfigurationError()


class GlpiApiHeadersHelper:
    def __init__(self, glpi_headers_data: GlpiApiHeadersData):
        self.__data: GlpiApiHeadersData = glpi_headers_data

    def create_request_headers(self):
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }

        if self.__data.app_token:
            headers['App-Token'] = self.__data.app_token

        if self.__data.user_token:
            headers['Authorization'] = f"user_token {self.__data.user_token}"

        if self.__data.session_token:
            headers['Session-Token'] = self.__data.session_token

        header_request = httpx.Headers(headers, 'UTF-8')
        return header_request


class GLPIApiClient:
    load_dotenv()
    _ENV_API_ENDPOINT = os.getenv('GLPI_API_ENDPOINT', 'http://localhost:8090/apirest.php')

    def __init__(
        self,
        username: str | None = None,
        password: str | None = None,
        server_endpoint: str | None = None,
        app_token: str | None = None,
        user_token: str | None = None,
        session_token: str | None = None,
    ) -> None:
        self.api_server_endpoint = server_endpoint or self._ENV_API_ENDPOINT
        self.__basic_auth: BasicAuth | None = None
        self.api_client = httpx.Client()

        if username and password:
            self.__basic_auth: BasicAuth = BasicAuth(username=username, password=password)
            self.api_client = httpx.Client(auth=self.__basic_auth.auth)

        self.auth_headers = GlpiApiHeadersHelper(
            glpi_headers_data=GlpiApiHeadersData(
                app_token=app_token,
                user_token=user_token,
                session_token=session_token,
            )
        )
        self.__session_token: str = ''
        self._init_session()

    def make_get(self, *args, **kwargs):
        return self.api_client.get(*args, **kwargs)

    def make_post(self, *args, **kwargs):
        return self.api_client.post(*args, **kwargs)


    def _init_session(self) -> None:
        endpoint = self.api_server_endpoint + '/initSession'
        response = self.api_client.post(endpoint, headers=self.auth_headers)

        if response.status_code == 200:
            self.__session_token = response.json()['session_token']
        else:
            raise InitSessionError()

    def request_error_handler(self, status_code: int, message: str):
        if status_code == 401:
            self._init_session()
            raise ClientGlpiError401()
        elif status_code == 400:
            # ! TODO: tratamento de erro para APP_TOKEN inválido
            raise ClientGlpiError400()
        elif status_code == 404:
            raise ClientGlpiError404()
        else:
            return message
