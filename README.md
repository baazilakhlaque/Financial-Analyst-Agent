# Financial Analyst Agent

An intelligent multi-agent system that automates stock market analysis, visualization and cloud storage using natural language queries. Built with CrewAI & AWS and integrated via Model Context Protocol (MCP) for seamless AI assistant integration.

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
- **AWS S3 Integration**: Automatically uploads generated charts to cloud storage

## Tech Stack
- **CrewAI**: Multi-agent orchestration 
- **OpenAI GPT-4o-mini**: Natural language understanding & code
- **FastMCP**: Fast Model Context Protocol framework for building MCP servers
- **Pydantic**: Type-safe query parsing 
- **AWS S3**: Cloud storage for generated visualizations

### Key Dependencies

- `crewai>=1.8.0` - Multi-agent framework
- `crewai-tools>=1.8.0` - Agent tools (CodeInterpreter, etc.)
- `fastmcp>=2.12.5` - MCP server framework
- `pydantic>=2.11.10` - Data validation
- `python-dotenv>=1.1.1` - Environment management
- `boto3>=1.34.0` - AWS SDK for S3 uploads

## Prerequisites

- **Python 3.12+**
- **uv** (recommended) or `pip` and `venv`
- **AWS Account** with S3 access ([Create one here](https://aws.amazon.com/))
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
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_REGION=us-east-1
AWS_S3_BUCKET_NAME=your-bucket-name
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

### AWS S3 Setup

#### 1. Create an S3 Bucket

1. Go to [AWS S3 Console](https://console.aws.amazon.com/s3/)
2. Click "Create bucket"
3. Name your bucket (e.g., `financial-analyst-plots`)
4. Select your region
5. Keep default settings and create

#### 2. Create IAM User with S3 Access

1. Go to [AWS IAM Console](https://console.aws.amazon.com/iam/)
2. Users → Create user
3. Attach policy: `AmazonS3FullAccess` (or a custom policy for least privilege)
4. Create access key (Application running outside AWS)
5. Copy **Access Key ID** and **Secret Access Key**

#### 3. Add Credentials to .env

AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=us-east-1
AWS_S3_BUCKET_NAME=financial-analyst-plots

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



