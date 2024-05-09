import streamlit as st 
from st_pages import Page, show_pages

def app():
    st.set_page_config(page_title="Foods delivery", 
                       layout="wide", 
                       initial_sidebar_state="expanded")
    
    show_pages(
        [
            Page("Pages/main_menu.py", "Place your order", "🍔"),
            Page("Pages/consult.py", "Consult orders", "🛒"),
        ]
    )
    
if __name__ == "__main__":
    app()