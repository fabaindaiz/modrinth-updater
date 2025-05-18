import logging
from enum import Enum
from typing import Optional

logger = logging.getLogger("ExceptionsLogger")

class STATUS(Enum):
    HTTP_200_OK = 200
    HTTP_400_BAD_REQUEST = 400
    HTTP_401_UNAUTHORIZED = 401
    HTTP_403_FORBIDDEN = 403
    HTTP_404_NOT_FOUND = 404
    HTTP_405_METHOD_NOT_ALLOWED = 405
    HTTP_408_REQUEST_TIMEOUT = 408
    HTTP_500_INTERNAL_SERVER_ERROR = 500
    HTTP_501_NOT_IMPLEMENTED = 501
    HTTP_502_BAD_GATEWAY = 502
    HTTP_503_SERVICE_UNAVAILABLE = 503
    HTTP_504_GATEWAY_TIMEOUT = 504

class HTTPException(Exception):
    def __init__(self, status_code: int, detail: Optional[str] = None):
        self.status_code = status_code
        self.detail = detail
        super().__init__(detail)

class HTTP_400_BAD_REQUEST(HTTPException):
    """Used when the user sends a malformed request"""
    def __init__(self, detail: Optional[str] = None):
        super().__init__(STATUS.HTTP_400_BAD_REQUEST.value, detail)
    
class HTTP_401_UNAUTHORIZED(HTTPException):
    """Used when the user is not authenticated"""
    def __init__(self, detail: Optional[str] = None):
        super().__init__(STATUS.HTTP_401_UNAUTHORIZED.value, detail)
    
class HTTP_403_FORBIDDEN(HTTPException):
    """Used when the user tries to access a resource that he is not allowed to"""
    def __init__(self, detail: Optional[str] = None):
        super().__init__(STATUS.HTTP_403_FORBIDDEN.value, detail)
    
class HTTP_404_NOT_FOUND(HTTPException):
    """Used when the requested resource is not found"""
    def __init__(self, detail: Optional[str] = None):
        super().__init__(STATUS.HTTP_404_NOT_FOUND.value, detail)

class HTTP_405_METHOD_NOT_ALLOWED(HTTPException):
    """Used when the method is not allowed"""
    def __init__(self, detail: Optional[str] = None):
        super().__init__(STATUS.HTTP_405_METHOD_NOT_ALLOWED.value, detail)
    
class HTTP_408_REQUEST_TIMEOUT(HTTPException):
    """Used when the request takes too long to process"""
    def __init__(self, detail: Optional[str] = None):
        super().__init__(STATUS.HTTP_408_REQUEST_TIMEOUT.value, detail)
    
class HTTP_500_INTERNAL_SERVER_ERROR(HTTPException):
    """Used when an unexpected error occurs"""
    def __init__(self, detail: Optional[str] = None):
        super().__init__(STATUS.HTTP_500_INTERNAL_SERVER_ERROR.value, detail)

class HTTP_501_NOT_IMPLEMENTED(HTTPException):
    """Used when the requested method is not implemented"""
    def __init__(self, detail: Optional[str] = None):
        super().__init__(STATUS.HTTP_501_NOT_IMPLEMENTED.value, detail)

class HTTP_502_BAD_GATEWAY(HTTPException):
    """Used when a request to another api fails"""
    def __init__(self, detail: Optional[str] = None):
        super().__init__(STATUS.HTTP_502_BAD_GATEWAY.value, detail)

class HTTP_504_GATEWAY_TIMEOUT(HTTPException):
    """Used when a request to another api takes too long to process"""
    def __init__(self, detail: Optional[str] = None):
        super().__init__(STATUS.HTTP_504_GATEWAY_TIMEOUT.value, detail)