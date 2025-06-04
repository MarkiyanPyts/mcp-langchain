# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python project that integrates LangChain with MCP (Model Context Protocol) adapters. The project uses `uv` as the package manager and requires Python 3.11 or higher.

## Development Commands

### Setup and Dependencies
```bash
# Install dependencies
uv sync

# Run the main script
uv run python main.py
```

### Python Environment
The project uses Python 3.11+ and manages dependencies via `uv` with a lockfile (`uv.lock`).

## Key Dependencies

- **langchain-mcp-adapters**: Core MCP adapter functionality for LangChain
- **langchain[openai]**: LangChain framework with OpenAI integration
- **langgraph**: Graph-based orchestration for LangChain
- **python-dotenv**: Environment variable management

## Architecture Notes

Currently, the project has a minimal structure with just a basic async main entry point in `main.py`. Future development will likely involve:
- MCP server/client implementation using langchain-mcp-adapters
- LangChain agent or chain implementations
- Integration with LangGraph for complex workflows