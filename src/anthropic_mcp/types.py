# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Typed models for Anthropic API responses."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class ModelInfo(BaseModel, frozen=True, slots=True):
    """Anthropic model info."""

    id: str
    name: str | None = None
    description: str | None = None


class MessageResponse(BaseModel, frozen=True, slots=True):
    """Message API response."""

    id: str | None = None
    type: str | None = None
    role: str | None = None
    content: list[dict[str, Any]] = Field(default_factory=list)


class TokenCount(BaseModel, frozen=True, slots=True):
    """Token count response."""

    tokens: int | None = None
    model: str | None = None


class BatchInfo(BaseModel, frozen=True, slots=True):
    """Batch job info."""

    id: str | None = None
    status: str | None = None
    created_at: int | None = None


# Type aliases
JSONPrimitive = Literal[str, int, float, bool, None]
JSONValue = JSONPrimitive | list["JSONValue"] | dict[str, "JSONValue"]
JSONObject = dict[str, JSONValue]