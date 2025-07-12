```markdown
# Stock Analyser

## Description
The Stock Analyser is a web-based application that provides detailed financial analysis and investment recommendations for stocks. Leveraging AI agents and real-time data retrieval, this tool analyzes stock symbols input by users to generate comprehensive insights into financial health and potential investment strategies.

## Features
- **Web Interface**: Simple and intuitive UI for inputting stock symbols and viewing results.
- **AI Agents**: Utilizes CrewAI agents to gather financial data, analyze it, and provide recommendations.
- **Dynamic Analysis**: Fetches real-time financial data and news for up-to-date analysis.
- **Investment Advice**: Provides actionable recommendations (Buy/Hold/Sell) based on analysis.
- **Markdown Reports**: Generates analysis and recommendation reports in markdown format.

## Prerequisites
- **Python 3.x**: Ensure Python is installed.
- **OpenAI API Key**: Necessary for AI-driven analysis.

## Setup Instructions

1. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   cd StockAnalyser
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## How to Run

1. **Start the Flask Application**:
   ```bash
   python app.py
   ```

2. **Access the Application**:
   - Open a web browser and go to `http://127.0.0.1:5000/`.
   - Enter a stock symbol and click "Analyze" to view the analysis results.

## Technologies Used
- **Flask**: For building the web application.
- **CrewAI**: To manage AI agents for data processing and analysis.
- **OpenAI**: Language model processing for analysis.
- **YFinance**: To fetch financial data.
- **Curl_cffi**: For HTTP requests.
- **Langchain**: Tools for language model workflows.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
```

This README.md provides a comprehensive guide to understanding, setting up, and running the Stock Analyser project, ensuring users can easily leverage the tool for financial analysis and investment recommendations.