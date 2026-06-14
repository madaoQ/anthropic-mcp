# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Message creation tools for Anthropic."""

from __future__ import annotations

from typing import Any

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from anthropic.guards import (
    validate_max_tokens,
    validate_message_content,
    validate_model,
    validate_temperature,
)
from anthropic.request import request
from anthropic.types import JSONObject


@tool(
    description="Create a message using Claude.",
    tags=["messages", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def anthropic_create_message(
    model: str = "claude-sonnet-4-20250514",
    messages: list[dict[str, str]] | None = None,
    system_message: str | None = None,
    max_tokens: int = 1024,
    temperature: float = 1.0,
    stream: bool = False,
) -> JSONObject:
    """Create a message with Claude.

    Args:
        model: Model to use (claude-opus-4, claude-sonnet-4, claude-haiku-4, etc.).
        messages: List of message objects with role and content.
        system_message: Optional system prompt.
        max_tokens: Maximum response tokens.
        temperature: Sampling temperature (0.0-1.0).
        stream: Whether to stream response.

    Returns:
        Message response from Claude.

    Raises:
        ValueError: If parameters are invalid.
        RuntimeError: If the API request fails.

    """
    validate_model(model)
    validate_temperature(temperature)
    validate_max_tokens(max_tokens)

    if messages is None:
        messages = []
    else:
        for msg in messages:
            if "content" in msg:
                validate_message_content(msg["content"])

    body: JSONObject = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "stream": stream,
    }

    if system_message:
        body["system"] = system_message

    result = await request(HttpMethod.POST, "/messages", body)
    return result


message_tools = [anthropic_create_message]