# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Model listing tools for Anthropic."""

from __future__ import annotations

from dedalus_mcp import tool
from dedalus_mcp.types import ToolAnnotations

from anthropic_mcp.types import ModelInfo, ModelList


@tool(
    description="List available Anthropic models.",
    tags=["models", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def anthropic_list_models() -> ModelList:
    """List available Anthropic models.

    Returns:
        List of available models with their IDs and descriptions.

    """
    # Anthropic doesn't have a list_models endpoint
    # Return known models based on documentation
    return ModelList(
        models=[
            ModelInfo(
                id="claude-opus-4-20250514",
                name="Claude Opus 4",
                description="Most capable model for complex tasks",
            ),
            ModelInfo(
                id="claude-sonnet-4-20250514",
                name="Claude Sonnet 4",
                description="Balanced for reasoning and speed",
            ),
            ModelInfo(
                id="claude-haiku-4-20250514",
                name="Claude Haiku 4",
                description="Fast, efficient for simple tasks",
            ),
            ModelInfo(
                id="claude-3-5-sonnet-20241022",
                name="Claude 3.5 Sonnet",
                description="Previous generation Sonnet",
            ),
            ModelInfo(
                id="claude-3-5-haiku-20241022",
                name="Claude 3.5 Haiku",
                description="Previous generation Haiku",
            ),
        ]
    )


model_tools = [anthropic_list_models]