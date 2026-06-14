# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Batch processing tools for Anthropic."""

from __future__ import annotations

from typing import Any

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from anthropic.guards import validate_batch_id
from anthropic.request import request
from anthropic.types import JSONObject


@tool(
    description="Create a batch of messages for async processing.",
    tags=["batches", "write"],
    annotations=ToolAnnotations(readOnlyHint=False),
)
async def anthropic_create_batch(
    requests: list[dict[str, Any]],
    metadata: dict[str, Any] | None = None,
) -> JSONObject:
    """Create a batch of requests.

    Args:
        requests: List of request objects.
        metadata: Optional metadata for tracking.

    Returns:
        Batch creation confirmation with ID.

    Raises:
        ValueError: If parameters are invalid.
        RuntimeError: If the API request fails.

    """
    if not requests:
        raise ValueError("Requests list cannot be empty")

    body: JSONObject = {
        "requests": requests,
    }

    if metadata is not None:
        body["metadata"] = metadata

    result = await request(HttpMethod.POST, "/batches", body)
    return result


@tool(
    description="Get status of a batch job.",
    tags=["batches", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def anthropic_get_batch(
    batch_id: str,
) -> JSONObject:
    """Get batch status.

    Args:
        batch_id: Batch ID to check.

    Returns:
        Batch status and results.

    Raises:
        ValueError: If batch_id is invalid.
        RuntimeError: If the API request fails.

    """
    validate_batch_id(batch_id)

    result = await request(HttpMethod.GET, f"/batches/{batch_id}")
    return result


@tool(
    description="Cancel a running batch job.",
    tags=["batches", "write"],
    annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=True),
)
async def anthropic_cancel_batch(
    batch_id: str,
) -> JSONObject:
    """Cancel a batch.

    Args:
        batch_id: Batch ID to cancel.

    Returns:
        Cancellation confirmation.

    Raises:
        ValueError: If batch_id is invalid.
        RuntimeError: If the API request fails.

    """
    validate_batch_id(batch_id)

    result = await request(HttpMethod.POST, f"/batches/{batch_id}/cancel", {})
    return result


batch_tools = [anthropic_create_batch, anthropic_get_batch, anthropic_cancel_batch]