from crewai import Agent
from datetime import datetime
from .tools import get_company_info, get_income_statements, get_current_stock_price, search_tool
from llm_config import llm 

Today = datetime.now().strftime("%d-%b-%Y")

news_info_explorer = Agent(
    role='News and Info Researcher',
    goal='Gather latest news about a company',
    llm=llm,
    tools=[search_tool],
    verbose=True,
    cache=True,
    max_iter=5,
    backstory=f"You are an expert researcher. Today is {Today}."
)

data_explorer = Agent(
    role='Data Researcher',
    goal='Get financial data about a stock',
    llm=llm,
    tools=[get_company_info, get_income_statements],
    verbose=True,
    cache=True,
    max_iter=5,
    backstory=f"You are a financial researcher. Today is {Today}."
)

analyst = Agent(
    role='Data Analyst',
    goal='Analyze financial and stock data',
    llm=llm,
    verbose=True,
    backstory=f"You analyze stock data and news. Use Indian units. Today is {Today}."
)

fin_expert = Agent(
    role='Financial Expert',
    goal='Recommend whether to buy/sell/hold a stock',
    llm=llm,
    tools=[get_current_stock_price],
    verbose=True,
    max_iter=5,
    backstory=f"You advise based on stock and company data. Today is {Today}."
)
