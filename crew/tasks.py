from crewai import Task
from .agents import data_explorer, news_info_explorer, analyst, fin_expert

get_company_financials = Task(
    description="Get income statements and financial data for {stock}",
    expected_output="Detailed financial data for {stock}.",
    agent=data_explorer,
)

get_company_news = Task(
    description="Get latest news about {stock}",
    expected_output="Summarized news and updates about the company.",
    agent=news_info_explorer,
)

analyse = Task(
    description="Analyze stock financials and news",
    expected_output="Full analysis in Indian number format (lakh/crore).",
    agent=analyst,
    context=[get_company_financials, get_company_news],
    output_file="output/Analysis.md"
)

advise = Task(
    description="Provide investment advice based on analysis",
    expected_output="Recommendation in markdown: Buy / Hold / Sell.",
    agent=fin_expert,
    context=[analyse],
    output_file="output/Recommendation.md"
)
