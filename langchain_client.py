from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY2"))


async def main():
    client = MultiServerMCPClient(
    {
        "math": {
            "command": "python",
            # Make sure to update to the full absolute path to your math_server.py file
            "args": ["/Users/markiyanpyts/Documents/GitHub/mcp-langchain/servers/math_server.py"],
            "transport": "stdio",
        },
        "weather": {
            # make sure you start your weather server on port 8000
            "url": "http://localhost:8000/mcp",
            "transport": "streamable_http",
        }
    }
    )
    tools = await client.get_tools()
    agent = create_react_agent("openai:gpt-4.1", tools)
    math_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
    weather_response = await agent.ainvoke({"messages": "what is the weather in nyc?"})
    print("Math Response:", math_response["messages"][-1].content)
    print("Weather Response:", weather_response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())
    print("Client initialized")
