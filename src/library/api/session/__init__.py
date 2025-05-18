from abc import ABC, abstractmethod
from aiohttp import ClientSession
from pydantic import SecretStr
from typing import Optional

class AuthorizedSession(ABC):
    """Base class for authorized sessions"""
    @abstractmethod
    async def headers(self, session: ClientSession, headers: dict = {}) -> dict:
        """Update the headers for the request with the authorization data.

        Args:
            session (ClientSession): ClientSession object for the request.
            headers (dict, optional): Original headers for the request. Defaults to {}.

        Returns:
            dict: Updated headers for the request with the authorization data included.
        """
        pass

class NoAuthSession(AuthorizedSession):
    """Session class for no authorization"""
    async def headers(self, session: ClientSession, headers: dict = {}) -> dict:
        return headers

class TokenSession(AuthorizedSession):
    """Session class for API key authorization
    
    Args:
        token (str): API key for authorization.
        """
    def __init__(self,
            token: str|SecretStr,
            scheme: Optional[str] = "Bearer ",
            parameter: str = "Authorization",
            ) -> None:
        if isinstance(token, str):
            token = SecretStr(token)
        self.__token: SecretStr = token
        self.__scheme: Optional[str] = scheme
        self.__parameter: str = parameter
        super().__init__()
    
    async def headers(self, session: ClientSession, headers: dict = {}) -> dict:
        headers.update({self.__parameter: f"{self.__scheme}{self.__token.get_secret_value()}"})
        return headers

NO_AUTHORIZE = NoAuthSession()