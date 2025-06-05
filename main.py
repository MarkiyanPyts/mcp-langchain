import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

stdio_server_params = StdioServerParameters(command="python", args=["/Users/markiyanpyts/Documents/GitHub/mcp-langchain/servers/math_server.py"])

async def main():
    print("Hello from mcp-langchain! ")
    
    # Initialize the LLM after environment variables are loaded
    llm = ChatOpenAI()
    
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("Session initialized")
            tools = await load_mcp_tools(session)
            #print("Tools:", tools)
            agent = create_react_agent(llm, tools)

            result = await agent.invoke(
                HumanMessage(
                    content="What is the sum of 2 and 3?"
                )
            )
            print("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
            print("Result:", result.messages[-1].content)
     


if __name__ == "__main__":
    asyncio.run(main())
