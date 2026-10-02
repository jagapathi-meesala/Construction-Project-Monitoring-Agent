"""Environment-only runtime configuration."""
from __future__ import annotations
import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    environment: str
    log_level: str
    timeout_seconds: int

    @classmethod
    def from_env(cls) -> "Settings":
        required = ("ENVIRONMENT", "LOG_LEVEL", "TOOL_TIMEOUT_SECONDS")
        missing = [key for key in required if not os.getenv(key)]
        if missing:
            raise ValueError("Missing required environment variables: " + ", ".join(missing))
        try:
            timeout = int(os.environ["TOOL_TIMEOUT_SECONDS"])
        except ValueError as exc:
            raise ValueError("TOOL_TIMEOUT_SECONDS must be an integer") from exc
        if timeout <= 0:
            raise ValueError("TOOL_TIMEOUT_SECONDS must be positive")
        return cls(os.environ["ENVIRONMENT"], os.environ["LOG_LEVEL"], timeout)
