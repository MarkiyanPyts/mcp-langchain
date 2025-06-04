import asyncio
from dotenv import load_dotenv
load_dotenv()
import os
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

async def main():
    print("Hello from mcp-langchain! ")


if __name__ == "__main__":
    asyncio.run(main())
