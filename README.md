# chatbot_web_wikipedia_search
This project is a chatbot web app that lets you search both the web (via Tavily API) and Wikipedia using a conversational interface powered by LLMs. Built with [Streamlit](https://streamlit.io/), [LangChain](https://python.langchain.com/), and [Groq’s Gemma2-9b-it model](https://groq.com/).

## Features

- 🔍 Search the web or Wikipedia from a single chat interface
- 🦜 Uses LangChain agents for smart tool selection
- 🌐 Integrates Tavily API for real-time web search
- 📚 Wikipedia search via LangChain tools
- ⚡ Fast, interactive UI with Streamlit

## How it works

1. Enter your question in the chat box.
2. Choose whether to search the Web or Wikipedia.
3. Click "Search" to get an answer powered by LLMs and the selected data source.
## Setup

1. **Clone the repo:**
    ```sh
    git clone https://github.com/yourusername/web-wikipedia-chatbot.git
    cd web-wikipedia-chatbot
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set your API keys:**
    - Add your Tavily API key to your environment variables or directly in the script (for demo purposes, a dev key is included).

4. **Run the app:**
    ```sh
    streamlit run LANGCHAIN_TOOLS/chatbot_web_wikipedia.py
## Example

![screenshot](screenshot.png)

## Tech Stack

- Python
- Streamlit
- LangChain
- Groq LLMs
- Tavily API
- Wikipedia API
