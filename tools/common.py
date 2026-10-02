from __future__ import annotations
from typing import Any, Mapping
from contracts.tool_contract import ToolInputError

def require_mapping(inputs: Mapping[str, Any]) -> None:
    if not isinstance(inputs, Mapping): raise ToolInputError("inputs must be an object")

def number(inputs: Mapping[str, Any], key: str, minimum: float | None = None, maximum: float | None = None) -> float:
    value = inputs.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)): raise ToolInputError(f"{key} must be numeric")
    value = float(value)
    if minimum is not None and value < minimum: raise ToolInputError(f"{key} must be >= {minimum}")
    if maximum is not None and value > maximum: raise ToolInputError(f"{key} must be <= {maximum}")
    return value

def text(inputs: Mapping[str, Any], key: str, max_len: int = 500) -> str:
    value = inputs.get(key)
    if not isinstance(value, str) or not value.strip(): raise ToolInputError(f"{key} must be a non-empty string")
    value = value.strip()
    if len(value) > max_len: raise ToolInputError(f"{key} exceeds maximum length of {max_len}")
    return value
