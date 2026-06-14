# Anthropic MCP Server

A Type 3 DAuth MCP server for [Anthropic API](https://console.anthropic.com). Provides access to Claude models, message creation, token counting, and batch processing.

## Features

- **List Models** — View available Claude models
- **Create Message** — Chat with Claude
- **Count Tokens** — Calculate token usage for text
- **Create Batch** — Submit batch jobs for async processing
- **Get Batch** — Check batch job status
- **Cancel Batch** — Cancel a running batch

## Authentication

This server uses **Type 3 DAuth** (Dedalus Auth) — your API key is encrypted client-side and decrypted in a secure Dedalus enclave.

### Get Your Anthropic API Key

1. Go to https://console.anthropic.com/settings/keys
2. Create a new API key
3. Copy the key

## Installation

```bash
git clone https://github.com/dedalus-labs/anthropic-mcp.git
cd anthropic-mcp
pip install -e .
cp .env.example .env
# Edit .env and add ANTHROPIC_API_KEY
```

## Available Tools

### `anthropic_list_models`

List available Claude models.

```python
anthropic_list_models()
```

### `anthropic_create_message`

Create a message with Claude.

```python
anthropic_create_message(
    model="claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=500,
    temperature=1.0,
)
```

### `anthropic_count_tokens`

Count tokens in text.

```python
anthropic_count_tokens(
    text="Hello, world!",
    model="claude-3-5-sonnet-20241022",
)
```

### `anthropic_create_batch`

Create a batch job.

```python
anthropic_create_batch(
    requests=[
        {"model": "claude-sonnet-4-20250514", "messages": [{"role": "user", "content": "Hi"}]},
    ],
    metadata={"source": "mcp"},
)
```

### `anthropic_get_batch`

Get batch status.

```python
anthropic_get_batch(batch_id="batch-id-here")
```

### `anthropic_cancel_batch`

Cancel a batch.

```python
anthropic_cancel_batch(batch_id="batch-id-here")
```

## Cost & Rate Limits

Anthropic uses per-token pricing. Check https://anthropic.com/pricing for current rates.

## Deploy to Dedalus

1. Push to GitHub (public repo)
2. Go to https://www.dedaluslabs.ai/dashboard
3. Add Server → Connect GitHub repo
4. Set `ANTHROPIC_API_KEY` as Required Credential
5. Deploy

## License

MIT