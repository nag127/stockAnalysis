from crewai.tools import tool
import json
import time
import yfinance as yf
from curl_cffi import requests
from langchain_community.tools import DuckDuckGoSearchRun

# Session with curl_cffi to impersonate a browser (bypasses some bot detection)
session = requests.Session(impersonate="chrome")


@tool("DuckDuckGo Search")
def search_tool(search_query: str) -> str:
    """Search the internet for information on a given topic using DuckDuckGo."""
    return DuckDuckGoSearchRun().run(search_query)


@tool("Get current stock price")
def get_current_stock_price(symbol: str) -> str:
    """Use this tool to get the current stock price for a given symbol.
    
    Args:
        symbol (str): The stock symbol.
    
    Returns:
        str: The current stock price or error message.
    """
    try:
        time.sleep(0.5)
        stock = yf.Ticker(symbol, session=session)
        current_price = stock.info.get("regularMarketPrice", stock.info.get("currentPrice"))
        return f"{current_price:.2f}" if current_price else f"Could not fetch current price for {symbol}"
    except Exception as e:
        return f"Error fetching current price for {symbol}: {e}"


@tool("Get company information")
def get_company_info(symbol: str) -> str:
    """Use this tool to get company profile and financial snapshot for a given stock symbol.
    
    Args:
        symbol (str): The stock symbol.
    
    Returns:
        str: A JSON-formatted string containing company info or an error message.
    """
    try:
        company_info_full = yf.Ticker(symbol, session=session).info
        if not company_info_full:
            return f"Could not fetch company info for {symbol}"

        company_info_cleaned = {
            "Name": company_info_full.get("shortName"),
            "Symbol": company_info_full.get("symbol"),
            "Current Stock Price": f"{company_info_full.get('regularMarketPrice', company_info_full.get('currentPrice'))} {company_info_full.get('currency', 'USD')}",
            "Market Cap": f"{company_info_full.get('marketCap', company_info_full.get('enterpriseValue'))} {company_info_full.get('currency', 'USD')}",
            "Sector": company_info_full.get("sector"),
            "Industry": company_info_full.get("industry"),
            "City": company_info_full.get("city"),
            "Country": company_info_full.get("country"),
            "EPS": company_info_full.get("trailingEps"),
            "P/E Ratio": company_info_full.get("trailingPE"),
            "52 Week Low": company_info_full.get("fiftyTwoWeekLow"),
            "52 Week High": company_info_full.get("fiftyTwoWeekHigh"),
            "50 Day Average": company_info_full.get("fiftyDayAverage"),
            "200 Day Average": company_info_full.get("twoHundredDayAverage"),
            "Employees": company_info_full.get("fullTimeEmployees"),
            "Total Cash": company_info_full.get("totalCash"),
            "Free Cash flow": company_info_full.get("freeCashflow"),
            "Operating Cash flow": company_info_full.get("operatingCashflow"),
            "EBITDA": company_info_full.get("ebitda"),
            "Revenue Growth": company_info_full.get("revenueGrowth"),
            "Gross Margins": company_info_full.get("grossMargins"),
            "Ebitda Margins": company_info_full.get("ebitdaMargins"),
        }

        return json.dumps(company_info_cleaned)
    except Exception as e:
        return f"Error fetching company profile for {symbol}: {e}"


@tool("Get income statements")
def get_income_statements(symbol: str) -> str:
    """Use this tool to get income statements for a given stock symbol.
    
    Args:
        symbol (str): The stock symbol.
    
    Returns:
        str: A JSON-formatted string of the income statements or error message.
    """
    try:
        stock = yf.Ticker(symbol, session=session)
        financials = stock.financials
        return financials.to_json(orient="index")
    except Exception as e:
        return f"Error fetching income statements for {symbol}: {e}"
