import sys
import logging
from fastmcp import FastMCP
from main import mcp

# Configure basic logging to stderr
logging.basicConfig(level=logging.ERROR, stream=sys.stderr)

if __name__ == "__main__":
    # Redirect stdout to stderr for logs and banner from FastMCP
    # Store old stdout to a variable if needed by FastMCP MCP stdio transport?
    # Actually, we shouldn't redirect stdout entirely as MCP uses stdout for JSON RPC.
    # But FastMCP prints its banner to stdout.
    # The better way is to pass `host="stdio"` or something similar, or see how fastmcp handles it.
    
    # We will just suppress logging banner by setting an environment variable or logging level
    import os
    os.environ["FASTMCP_LOG_LEVEL"] = "ERROR"
    os.environ["RICH_DISABLE"] = "1" # FastMCP uses rich for banner
    
    # run MCP server
    # FastMCP logging over stdio can corrupt MCP protocol JSON RPC messages.
    # To fix this, we'll patch fastmcp's logger before running.
    import logging
    logging.getLogger("fastmcp").setLevel(logging.CRITICAL)
    
    # Fastmcp prints a rich banner.
    import builtins
    original_print = builtins.print
    builtins.print = lambda *args, **kwargs: None
    
    try:
        mcp.run(transport="stdio")
    finally:
        builtins.print = original_print
