# ./adk_agent_samples/mcp_agent/agent.py
import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters,StdioConnectionParams

api_client_id = os.environ.get("MCP_API_CLIENT_ID")
api_client_secret = os.environ.get("MCP_API_CLIENT_SECRET")



root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='mongodb_mcp_server_agent',
    instruction='Assist the user with MongoDB database management, queries, and server operations.',
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command='npx',
                    args=[
                        "-y",
                        "mongodb-mcp-server",
                        "--apiClientId",
                        api_client_id,
                        "--apiClientSecret",
                        api_client_secret
                    ],
                )
            ),
        )
    ],
)


