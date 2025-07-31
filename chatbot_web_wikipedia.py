from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv
from langchain_tavily import TavilySearch
import os
from langchain.agents import create_react_agent,AgentExecutor
from langchain import hub
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()

from langchain_tavily import TavilySearch

load_dotenv()
llm = ChatGroq(model="gemma2-9b-it")


# Initialize Wikipedia tool
wiki_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
search_tool = TavilySearch(
    max_results=5,
    topic="general",
    # include_answer=False,
    # include_raw_content=False,
    # include_images=False,
    # include_image_descriptions=False,
    # search_depth="basic",
    # time_range="day",
    # include_domains=None,
    # exclude_domains=None
)

prompt=hub.pull("hwchase17/react") #pulls  react agent prompt


st.header('Web and Wikipedia Search tool')
user_input=st.text_input("Ask me anything I will search it on web and wikipedia")
searchArea_input=st.selectbox("Select where you want to search either on Web or Wikipedia",["Web","Wikipedia"])

if st.button('Search') and user_input:
    selected_tool = search_tool if searchArea_input == "Web" else wiki_tool
    
    agent=create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=prompt
    )
    agent_executor=AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose=True
    )
    
    
    response = agent_executor.invoke({"input": user_input})
    
    st.write(response)

 
