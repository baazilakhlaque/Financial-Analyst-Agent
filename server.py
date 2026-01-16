from fastmcp import FastMCP
from financial_analyst_agent import run_financial_analysis


mcp = FastMCP("financial-analyst-agent")

@mcp.tool
def analyze_stock(query: str) -> str:
    """
    Analyzes the stock market data based on the user query and generates executable python code to visualize the stock data.
    Returns a formatted python script which is ready for execution.
    The query is a string that must contain the stock symbol (e.g., TSLA, NVDA, MSFT, etc.), 
    timeframe (e.g., 1d, 1mo, 1y), and action to perform (e.g., plot, analyze, compare).
    
    Args:
        query: The user query to analyze the stock market data.
    Returns:
        str: A formatted python script which is ready for execution.
    
    Here are some examples of valid queries:
    - "Show Tesla's stock performance over the last 6 months"
    - "Compare Apple and Qualcomm stocks for the past year"
    - "Analyze the trading volume of Nvidia stock for the last month"
    """

    try:
        result = run_financial_analysis(query)
        return result
    except Exception as e:
        return f"Error: {e}"


@mcp.tool
def save_code(code: str) -> str:
    """ 
    The input is a working, executable python code in string format.
    Saves the generated python code to the 'stock_analysis.py' file.
    Makes sure that the code is a valid python file, ready for execution.

    Args:
        code -> str: The generated python code to save.
    
    Returns:
        str: A message indicating the code has been saved.
    
    """

    file_path = "stock_analysis.py"
    try:
        with open(file_path, "w") as f:
            f.write(code)
        return f"Code saved to {file_path}"
    except Exception as e:
        return f"Error: {e}"

@mcp.tool
def execute_code() -> str:
    """
    Executes the python code saved in the 'stock_analysis.py' file.
    Returns the output of the code execution.

    Args:
        None
    
    Returns:
        str: The output of the code execution.
    
    """
    try:
        with open("stock_analysis.py", "r") as f:
            exec(f.read())
        return "Code executed successfully"
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    mcp.run()
    

