# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Token counting tools for Anthropic."""

from __future__ import annotations

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from anthropic.guards import validate_message_content, validate_model
from anthropic.request import request
from anthropic.types import JSONObject


@tool(
    description="Count tokens in text for Claude models.",
    tags=["tokens", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def anthropic_count_tokens(
    text: str,
    model: str = "claude-3-5-sonnet-20241022",
) -> JSONObject:
    """Count tokens in text.

    Args:
        text: Text to count tokens for.
        model: Model to use for tokenization.

    Returns:
        Token count.

    Raises:
        ValueError: If parameters are invalid.
        RuntimeError: If the API request fails.

    """
    validate_message_content(text)
    validate_model(model)

    body: JSONObject = {
        "model": model,
        "text": text,
    }

    result = await request(HttpMethod.POST, "/count_tokens", body)
    return result


token_tools = [anthropic_count_tokens]