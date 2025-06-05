import asyncio

from dotenv import load_dotenv

load_dotenv()
import os

from langchain_mcp_adapters import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

async def main():
    print("Hello from mcp-langchain! ")


if __name__ == "__main__":
    asyncio.run(main())
