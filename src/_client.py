# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Direct API testing client for Anthropic MCP.

This module is used for local testing without going through the MCP server.
"""

from __future__ import annotations

import asyncio
import os

import httpx
from dotenv import load_dotenv

load_dotenv()


async def test_create_message() -> None:
    """Test create_message endpoint."""
    print("Testing anthropic_create_message...")

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment")
        return

    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json",
    }

    body = {
        "model": "claude-sonnet-4-20250514",
        "messages": [{"role": "user", "content": "Say hello in one word"}],
        "max_tokens": 10,
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "https://api.anthropic.com/v1/messages",
            headers=headers,
            json=body,
            timeout=30,
        )

    if resp.status_code == 200:
        data = resp.json()
        print(f"✓ Create message successful")
        content = data.get("content", [])
        if content:
            print(f"  Response: {content[0].get('text', 'N/A')}")
    else:
        print(f"✗ Error {resp.status_code}: {resp.text[:200]}")


async def main() -> None:
    """Run all direct API tests."""
    print("=" * 50)
    print("Anthropic Direct API Tests")
    print("=" * 50)
    print()

    await test_create_message()

    print()
    print("=" * 50)
    print("Tests completed!")


if __name__ == "__main__":
    asyncio.run(main())