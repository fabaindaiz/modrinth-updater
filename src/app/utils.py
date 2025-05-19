import os
from enum import Enum

class ENVIRONMENT(Enum):
    DEVELOPMENT = "DEVELOPMENT"
    PRODUCTION = "PRODUCTION"

    @staticmethod
    def from_str(environment: str) -> "ENVIRONMENT":
        return ENVIRONMENT(environment)
    
    @staticmethod
    def from_env() -> "ENVIRONMENT":
        return ENVIRONMENT(os.getenv("ENVIRONMENT", "PRODUCTION"))