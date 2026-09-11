"""Read-only MCP handshake and Resolve status check."""
import asyncio
import argparse
import json
import os
import sys
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

ROOT = Path(__file__).resolve().parents[1]

async def main(server_only=False):
    env = dict(os.environ)
    env.update({
        "RESOLVE_SCRIPT_API": "C:/ProgramData/Blackmagic Design/DaVinci Resolve/Support/Developer/Scripting",
        "RESOLVE_SCRIPT_LIB": "C:/Program Files/Blackmagic Design/DaVinci Resolve/fusionscript.dll",
        "DAVINCI_RESOLVE_MCP_UPDATE_CHECK": "0",
    })
    server = StdioServerParameters(command=sys.executable,
        args=[str(ROOT / "mcp/davinci-resolve/src/server.py")], env=env)
    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print(json.dumps({"mcp_handshake": "ok", "tools": len(tools.tools)}))
            if server_only:
                return 0
            result = await session.call_tool("project_manager", {"action": "get_current"})
            print(result.model_dump_json())
            payload = (result.structuredContent or {}).get("result", {})
            if result.isError or payload.get("error"):
                return 2
            return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--server-only", action="store_true", help="Check MCP startup without querying Resolve")
    args = parser.parse_args()
    sys.exit(asyncio.run(asyncio.wait_for(main(args.server_only), timeout=45)))
