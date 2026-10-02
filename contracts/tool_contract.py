"""Framework-independent tool contract."""
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Mapping

class ToolInputError(ValueError):
    pass

@dataclass(frozen=True)
class ToolMetadata:
    name: str
    description: str
    input_schema: Mapping[str, Any]

@dataclass
class ToolResult:
    success: bool
    data: dict[str, Any] = field(default_factory=dict)
    error: dict[str, Any] | None = None

class Tool(ABC):
    metadata: ToolMetadata

    @abstractmethod
    def validate(self, inputs: Mapping[str, Any]) -> dict[str, Any]: ...

    @abstractmethod
    def execute(self, inputs: Mapping[str, Any]) -> ToolResult: ...

    def run(self, inputs: Mapping[str, Any]) -> ToolResult:
        try:
            validated = self.validate(inputs)
            return self.execute(validated)
        except ToolInputError as exc:
            return ToolResult(False, error={"type": "validation_error", "message": str(exc)})
        except Exception as exc:
            return ToolResult(False, error={"type": "execution_error", "message": str(exc)})
