# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Input validation for Anthropic API parameters."""

from __future__ import annotations

import re


# Anthropic model names: alphanumeric, hyphens, dots
_MODEL_RE = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9_.-]*$")


def validate_model(model: str) -> None:
    """Validate an Anthropic model name."""
    if not model or not _MODEL_RE.match(model):
        msg = f"Invalid model name: {model!r}"
        raise ValueError(msg)


def validate_temperature(temperature: float) -> None:
    """Validate temperature parameter."""
    if not 0.0 <= temperature <= 1.0:
        msg = f"Temperature must be between 0.0 and 1.0, got {temperature}"
        raise ValueError(msg)


def validate_max_tokens(max_tokens: int) -> None:
    """Validate max_tokens parameter."""
    if max_tokens < 1:
        msg = f"max_tokens must be at least 1, got {max_tokens}"
        raise ValueError(msg)


def validate_message_content(content: str) -> None:
    """Validate message content."""
    if not content or not content.strip():
        msg = "Message content cannot be empty"
        raise ValueError(msg)


def validate_batch_id(batch_id: str) -> None:
    """Validate a batch ID."""
    if not batch_id or not batch_id.strip():
        msg = "Batch ID cannot be empty"
        raise ValueError(msg)