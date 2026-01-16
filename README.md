# Financial Analyst Agent

An intelligent multi-agent system that automates stock market analysis and visualization using natural language queries. Built with CrewAI and integrated via Model Context Protocol (MCP) for seamless AI assistant integration.

## Problem

Traditional stock market analysis requires:
- **Manual data retrieval** from multiple sources
- **Complex code writing** for data visualization
- **Domain expertise** in both finance and programming
- **Time-consuming** process from query to visualization

Users want to ask simple questions like *"Show me Tesla's stock performance over the last 6 months"* and get actionable insights **without writing code or understanding financial APIs**.

## Solution

This project automates the entire stock analysis workflow using a **multi-agent AI system**:

1. **Natural Language Processing**: Understands plain English queries about stocks
2. **Intelligent Parsing**: Extracts stock symbols, timeframes, and analysis requirements
3. **Code Generation**: Automatically creates production-ready Python visualization code
4. **Code Execution**: Validates and executes code with error handling
5. **Seamless Integration**: Works directly within AI assistants via MCP (Model Context Protocol)

**Result**: Users get professional-grade stock analysis and visualizations in seconds, just by asking.

## Features

- **Natural Language Interface**: Ask questions in plain English
- **Automatic Visualization**: Generates matplotlib charts and graphs
- **Code Generation & Execution**: Creates and runs Python code automatically
- **Error Recovery**: Agents fix code errors automatically
- **MCP Integration**: Works with Cursor, Claude Desktop, and other MCP-compatible tools


## Tech Stack
- **CrewAI**: Multi-agent orchestration 
- **OpenAI GPT-4o-mini**: Natural language understanding & code
- **FastMCP**: Fast Model Context Protocol framework for building MCP servers
- **Pydantic**: Type-safe query parsing 

### Key Dependencies

- `crewai>=1.8.0` - Multi-agent framework
- `crewai-tools>=1.8.0` - Agent tools (CodeInterpreter, etc.)
- `fastmcp>=2.12.5` - MCP server framework
- `pydantic>=2.11.10` - Data validation
- `python-dotenv>=1.1.1` - Environment management

## Prerequisites

- **Python 3.12+**
- **uv** (recommended) or `pip` and `venv`
- **OpenAI API Key** ([Get one here](https://platform.openai.com/api-keys))
- **Cursor** or another MCP-compatible client (optional, for integration)


## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd MCP-Financial-Analyst
```

### 2. Install uv (Recommended)
```bash
# macOS
brew install uv

# Or via pip
pip install uv

# Or standalone installer
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. Install Dependencies

```bash
# Using uv (recommended)
uv sync
```

Or using traditional pip
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt  # If you have one, or install manually
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env 
# Required
OPENAI_API_KEY=your_openai_api_key_here
```

## Configuration

### MCP Server Configuration (for Cursor)

Add to your `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "financial-analyst": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/MCP-Financial-Analyst",
        "run",
        "server.py"
      ]
    }
  }
}
```

After updating `mcp.json`, **restart Cursor** for changes to take effect.

## Usage

### Via MCP (Cursor/AI Assistant)

1. **Start Cursor** (or your MCP client)
2. **Ask natural language questions**:
   - "Show Tesla's stock performance over the last 6 months"
   - "Compare Apple and Qualcomm stocks for the past year"
   - "Analyze the trading volume of Nvidia stock for the last month"

The AI assistant will use the MCP tools (`analyze_stock`, `save_code`, `execute_code`) automatically.

### Command Line Testing
Using uv (recommended)

```bash
uv run python financial_analyst_agent.py
```
Or with activated venv
```bash
source .venv/bin/activate
python financial_analyst_agent.py
```

### Testing MCP server through MCP inspector
```bash
# Using uv
uv run fastmcp dev server.py
```

```bash
# Or direct execution
uv run python server.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



