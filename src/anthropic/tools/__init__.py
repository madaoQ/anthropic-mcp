# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Tool registry for anthropic-mcp.

Modules:
  models     -- anthropic_list_models
  messages   -- anthropic_create_message
  tokens     -- anthropic_count_tokens
  batches    -- anthropic_create_batch, anthropic_get_batch, anthropic_cancel_batch
"""

from __future__ import annotations

from anthropic.tools.batches import batch_tools
from anthropic.tools.messages import message_tools
from anthropic.tools.models import model_tools
from anthropic.tools.tokens import token_tools

anthropic_tools = [
    *model_tools,
    *message_tools,
    *token_tools,
    *batch_tools,
]