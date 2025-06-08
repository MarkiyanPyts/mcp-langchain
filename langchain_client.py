from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY2"))


async def main():
    async with MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [
                    "/Users/markiyanpyts/Documents/GitHub/mcp-langchain/servers/math_server.py"
                ],
            },
            "weather": {
                "url": "http://127.0.0.1:8000",
                "transport": "sse",
            },
        }
    ) as client:
        agent = create_react_agent(llm, client.get_tools())
        result = await agent.ainvoke(
            {
                "messages": "What is the sum of 54 + 10 * 2? "
            }
        )
        print("Result:", result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
    print("Client initialized")
