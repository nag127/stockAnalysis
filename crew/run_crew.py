from crewai import Crew, Process
from .agents import data_explorer, news_info_explorer, analyst, fin_expert
from .tasks import get_company_financials, get_company_news, analyse, advise
from datetime import datetime

def timestamp(msg):
    print(f"[{datetime.now()}] {msg}")

def run_crew_with_symbol(stock_symbol: str):
    # Inject stock symbol into tasks
    get_company_financials.description = get_company_financials.description.format(stock=stock_symbol)
    get_company_news.description = get_company_news.description.format(stock=stock_symbol)

    crew = Crew(
        agents=[data_explorer, news_info_explorer, analyst, fin_expert],
        tasks=[get_company_financials, get_company_news, analyse, advise],
        verbose=True,
        Process=Process.sequential,
        step_callback=timestamp
    )
    crew.kickoff()
