# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Anthropic MCP server for Dedalus.

Provides Claude messaging, token counting, and batch processing via Anthropic API.
Credentials provided by clients at runtime via DAuth token exchange.
"""

from __future__ import annotations

from anthropic_mcp.config import create_anthropic_connection
from anthropic_mcp.tools import anthropic_tools

__all__ = ["create_anthropic_connection", "anthropic_tools"]