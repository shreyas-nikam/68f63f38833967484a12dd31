import streamlit as st
from application_pages import page1, page2, page3

st.set_page_config(page_title="AI Career Navigator & Pathway Planner", layout="wide")

st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["AI Readiness Score Calculator", "What-If Scenario Analysis", "Data Explorer"])
st.sidebar.divider()

st.title("AI Career Navigator & Pathway Planner")
st.divider()

st.markdown(\"\"\"
This application implements the AI-Readiness Score (AI-R) framework, allowing users to understand, calculate, and simulate their career readiness in AI-driven labor markets. It provides an interactive environment to explore the impact of individual capabilities, market opportunities, and learning pathways on career prospects.

### Learning Goals
- Understand the key insights contained in the uploaded document and supporting data.
- Decompose the AI-Readiness Score into its systematic opportunity ($H^R$), idiosyncratic readiness ($V^R$), and synergy components.
- Evaluate the potential impact of various learning pathways on individual skill development and career readiness.
- Analyze different career paths based on market demand and personal capabilities through "what-if" scenarios.
\"\"\")

if page == "AI Readiness Score Calculator":
    page1.run_page1()
elif page == "What-If Scenario Analysis":
    page2.run_page2()
elif page == "Data Explorer":
    page3.run_page3()