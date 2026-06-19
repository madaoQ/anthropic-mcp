# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Typed models for Anthropic API responses."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class ModelInfo(BaseModel):
    """Anthropic model info."""
    model_config = _FROZEN_SLOT


    id: str
    name: str | None = None
    description: str | None = None


class MessageResponse(BaseModel):
    """Message API response."""
    model_config = _FROZEN_SLOT


    id: str | None = None
    type: str | None = None
    role: str | None = None
    content: list[dict[str, Any]] = Field(default_factory=list)


class TokenCount(BaseModel):
    """Token count response."""
    model_config = _FROZEN_SLOT


    tokens: int | None = None
    model: str | None = None


class BatchInfo(BaseModel):
    """Batch job info."""
    model_config = _FROZEN_SLOT


    id: str | None = None
    status: str | None = None
    created_at: int | None = None


# Type aliases
JSONPrimitive = Literal[str, int, float, bool, None]
JSONValue = JSONPrimitive | list["JSONValue"] | dict[str, "JSONValue"]
JSONObject = dict[str, JSONValue]