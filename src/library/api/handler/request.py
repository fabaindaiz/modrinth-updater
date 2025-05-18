from abc import ABC, abstractmethod
from typing import Any, TypeVar
from src.library.api.exceptions import HTTP_400_BAD_REQUEST

REQUEST = TypeVar('REQUEST', bound="RequestHandler")

class RequestHandler(ABC):
    """Abstract class for handling request data"""
    def set_use_body(self, use_body: bool) -> None:
        """Set the use_body flag for the request.

        Args:
            use_body (bool): Flag to determine if the request uses a body.
        """
        self.use_body = use_body

    @abstractmethod
    async def kwargs(self, query: dict[str, Any], body: dict[str, Any], kwargs: dict) -> dict:
        """Update the kwargs for the request with the request data.

        Args:
            data (dict): Body parameters for the request.
            kwargs (dict): Original kwargs for the request.

        Returns:
            dict: Updated kwargs for the request with the data included.
        """
        pass

    @abstractmethod
    async def headers(self, headers: dict = {}) -> dict:
        """Update the headers for the request with content type.

        Args:
            headers (dict, optional): Original headers for the request. Defaults to {}.

        Returns:
            dict: Updated headers for the request.
        """
        pass

class JsonRequest(RequestHandler):
    """Send JSON data in the request body"""
    async def kwargs(self, query: dict[str, Any], body: dict[str, Any], kwargs: dict) -> dict:
        if not self.use_body and body:
            raise HTTP_400_BAD_REQUEST("body is not allowed in this requests")
        kwargs.update({
            "json": body,
            "params": query,
        })
        return kwargs

    async def headers(self, headers: dict = {}) -> dict:
        headers.update({"Content-Type": "application/json"} if self.use_body else {})
        return headers

class MultiPartRequest(RequestHandler):
    """Send MultiPart data in the request body"""
    async def kwargs(self, query: dict[str, Any], body: dict[str, Any], kwargs: dict) -> dict:
        if not self.use_body:
            raise HTTP_400_BAD_REQUEST("MultiPartRequest requires a method that uses a body")
        kwargs.update({
            "json": body,
            "params": query,
        })
        return kwargs

    async def headers(self, headers: dict = {}) -> dict:
        headers.update({"Content-Type": "multipart/form-data"})
        return headers