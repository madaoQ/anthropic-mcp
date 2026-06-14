# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Anthropic API configuration."""

from dedalus_mcp.auth import Connection, SecretKeys

# Anthropic API base URL
ANTHROPIC_API_BASE = "https://api.anthropic.com/v1"


def create_anthropic_connection() -> Connection:
    """Create a DAuth connection to Anthropic API.

    Uses Bearer token authentication with x-api-key header.
    The API key is encrypted client-side and decrypted in the Dedalus enclave.

    Returns:
        Configured Connection for Anthropic API.

    """
    return Connection(
        name="anthropic",
        secrets=SecretKeys(token="ANTHROPIC_API_KEY"),
        base_url=ANTHROPIC_API_BASE,
        auth_header_format="Bearer {api_key}",
        auth_header_name="x-api-key",
    )