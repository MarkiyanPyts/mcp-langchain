from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import asyncio
import traceback

print("Starting langchain_client_debug.py...")

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY2")
print(f"API Key loaded: {'Yes' if api_key else 'No'}")

try:
    llm = ChatOpenAI(api_key=api_key)
    print("ChatOpenAI initialized successfully")
except Exception as e:
    print(f"Error initializing ChatOpenAI: {e}")
    traceback.print_exc()


async def main():
    print("\n=== Starting main() function ===")
    
    try:
        print("Creating MultiServerMCPClient...")
        client = MultiServerMCPClient(
            {
                "math": {
                    "command": "python",
                    "args": ["/Users/markiyanpyts/Documents/GitHub/mcp-langchain/servers/math_server.py"],
                    "transport": "stdio",
                },
                "weather": {
                    "url": "http://localhost:8000/mcp",
                    "transport": "streamable_http",
                }
            }
        )
        print("MultiServerMCPClient created successfully")
        
        print("\nGetting tools from client...")
        tools = await client.get_tools()
        print(f"Tools retrieved: {len(tools)} tools")
        for i, tool in enumerate(tools):
            print(f"  Tool {i+1}: {tool.name if hasattr(tool, 'name') else tool}")
        
        print("\nCreating agent...")
        # Fix: The first argument should be the llm object, not a string
        agent = create_react_agent(llm, tools)
        print("Agent created successfully")
        
        print("\nInvoking math query...")
        math_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
        print(f"Math response received: {math_response}")
        
        print("\nInvoking weather query...")
        weather_response = await agent.ainvoke({"messages": "what is the weather in nyc?"})
        print(f"Weather response received: {weather_response}")
        
        print("\n=== RESULTS ===")
        print("Math Response:", math_response["messages"][-1].content)
        print("Weather Response:", weather_response["messages"][-1].content)
        
    except Exception as e:
        print(f"\n!!! ERROR in main(): {type(e).__name__}: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    print("\nRunning async main...")
    try:
        asyncio.run(main())
        print("\nAsync main completed")
        print("Client initialized")
    except Exception as e:
        print(f"\n!!! ERROR in asyncio.run(): {type(e).__name__}: {e}")
        traceback.print_exc()