from enum import Enum
from abc import ABC, abstractmethod
from typing import Any, Optional, TypeVar
from aiohttp import ClientResponse

RESPONSE = TypeVar('RESPONSE', bound="ResponseHandler")

class ResponseHandler(ABC):
    """Abstract class for handling response data"""
    FAKE_RESPONSE: Any

    def __init__(self) -> None:
        self._response: Optional[ClientResponse] = None

    @abstractmethod
    async def set_response(self, response: Any) -> None:
        """Set the response object with the data from the request.

        Args:
            response (Any): Response object from the request.
        """
        pass

    @abstractmethod
    async def handle(self, response: ClientResponse) -> None:
        """Receive and process the response data from the request.

        Args:
            response (ClientResponse): ClientResponse object from the request.
        """
        pass

    @abstractmethod
    async def headers(self, headers: dict = {}) -> dict:
        """Update the headers for the request with accept.

        Args:
            headers (dict, optional): Original headers for the request. Defaults to {}.

        Returns:
            dict: Updated headers for the request.
        """
        pass

    def response(self) -> Optional[ClientResponse]:
        return self._response

class JsonResponse(ResponseHandler):
    """Receive JSON data from the response body"""
    FAKE_RESPONSE: Any = {"successful": True, "message": "Fake Response", "data": {}}

    def __init__(self) -> None:
        self._json: Optional[dict] = None

    async def set_response(self, response: Any) -> None:
        self._json = dict(response)

    async def handle(self, response: ClientResponse) -> None:
        self._json = await response.json()
        self._response = response

    async def headers(self, headers: dict = {}) -> dict:
        headers.update({"Accept": "application/json"})
        return headers
    
    def json(self) -> dict:
        """Return the JSON data from the response body.

        Returns:
            Optional[dict]: JSON data from the response body.
        """
        if self._json is None:
            raise ValueError("Response has not data.")
        return self._json

class StreamFormat(Enum):
    """Stream data format for the StreamResponse"""
    OCTET_STREAM = "application/octet-stream"
    XTARGZ = "application/x-targz"

class StreamResponse(ResponseHandler):
    """Receive Stream data from the response body"""
    FAKE_RESPONSE: Any = b""

    def __init__(self, format: StreamFormat = StreamFormat.OCTET_STREAM) -> None:
        self._stream: Optional[bytes] = None
        self._format: StreamFormat = format
    
    async def set_response(self, response: Any) -> None:
        self._stream = bytes(response)

    async def handle(self, response: ClientResponse) -> None:
        self._stream = await response.read()
        self._response = response

    async def headers(self, headers: dict = {}) -> dict:
        headers.update({"Accept": self._format.value})
        return headers
    
    def stream(self) -> bytes:
        """Return the stream data from the response body.

        Returns:
            Optional[bytes]: Byte stream data from the response body.
        """
        if self._stream is None:
            raise ValueError("Response has not data.")
        return self._stream