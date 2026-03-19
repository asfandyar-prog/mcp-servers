# 🔌 MCP Servers

<div align="center">

![MCP](https://img.shields.io/badge/MCP-Model_Context_Protocol-6C63FF?style=for-the-badge&logo=anthropic&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastMCP](https://img.shields.io/badge/FastMCP-1.26.0-00C896?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**Production-grade MCP servers built from scratch — connecting LLMs to real-world tools.**

[Overview](#-overview) • [Servers](#-servers) • [Getting Started](#-getting-started) • [Architecture](#-architecture) • [Connect](#-connect-to-claude-desktop)

</div>

---

## 🧠 Overview

This repository contains a growing collection of **Model Context Protocol (MCP) servers** — lightweight, tool-calling backends that give LLMs like Claude structured access to external capabilities.

MCP is to AI agents what REST is to web apps: a **standardized protocol** for exposing tools, resources, and prompts to language models.

```
LLM Client (Claude Desktop / Cursor)
        │
        │  JSON-RPC over stdio / SSE
        ▼
  MCP Server (this repo)
        │
        ▼
  Tool Logic (APIs, math, files, databases...)
```

---

## 📦 Servers

| Server | Description | Tools | Status |
|--------|-------------|-------|--------|
| `my-first-mcp-server` | Calculator server using FastMCP | `add` | ✅ Complete |
| _more coming soon..._ | | | 🔧 In Progress |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- `pip install mcp`

### Clone the repo

```bash
git clone https://github.com/asfandyar-prog/mcp-servers.git
cd mcp-servers
```

### Run a server

```bash
cd my-first-mcp-server
python fastmcp_calculator.py
```

> ⚠️ Running directly in terminal will show JSON errors — this is **expected**. MCP servers are designed to communicate with an MCP client, not the terminal. See [Connect to Claude Desktop](#-connect-to-claude-desktop) below.

---

## 🏗 Architecture

Each server follows this structure:

```
mcp-servers/
├── my-first-mcp-server/
│   └── fastmcp_calculator.py   # FastMCP server with tool definitions
├── README.md
```

### How a tool is defined

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-first-server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

mcp.run()
```

That's it — FastMCP handles all the JSON-RPC plumbing automatically.

---

## 🖥 Connect to Claude Desktop

To use any server with **Claude Desktop**, add it to your config file:

**Location:** `C:\Users\<YOU>\AppData\Roaming\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["C:\\Users\\<YOU>\\mcp-servers\\my-first-mcp-server\\fastmcp_calculator.py"]
    }
  }
}
```

Restart Claude Desktop → look for the 🔨 hammer icon → your tools are live.

---

## 🔗 Related Repositories

> Part of a broader AI engineering portfolio:

- [`agentic-systems-with-langgraph`](https://github.com/asfandyar-prog/agentic-systems-with-langgraph) — Multi-agent systems with LangGraph
- [`framework-free-agent`](https://github.com/asfandyar-prog/framework-free-agent) — Autonomous ReAct agent from scratch
- [`DeepLearning`](https://github.com/asfandyar-prog/DeepLearning) — Transformers, CNNs, from-scratch implementations

---

## 👤 Author

**Asfand Yar** — AI Engineer | Multi-Agent Systems | LLM Infrastructure

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/asfand-yar-3966b8291)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat&logo=github)](https://github.com/asfandyar-prog)
[![Email](https://img.shields.io/badge/Email-Contact-EA4335?style=flat&logo=gmail)](mailto:asfandyar@mailbox.unideb.hu)

---

<div align="center">
<sub>Built with ☕ in Debrecen, Hungary</sub>
</div>
