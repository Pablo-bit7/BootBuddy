#!/usr/bin/env python3
import streamlit as st

# Sidebar Navigation
def sidebar_navigation():
    st.sidebar.title("BootBuddy")
    st.sidebar.image("assets/bootbuddy_logo.png", width=150)  # Add your logo here
    st.sidebar.write("Navigation")

    # Menu items
    selection = st.sidebar.radio("Go to", ["Dashboard", "Team", "Feedback"])
    return selection

# Render the Dashboard page
def dashboard():
    st.title("Hello Campers 👋")
    st.write("This will display bootcamp content once we embed Google Docs.")

# Render the Team page (for future features)
def team():
    st.title("Your Team")
    st.write("Team information will go here.")

# Render the Feedback page (for future features)
def feedback():
    st.title("Feedback")
    st.write("Feedback form or link will go here.")

# Dashboard logic based on user choice
def dashboard_logic():
    # Sidebar navigation
    page = sidebar_navigation()

    if page == "Dashboard":
        dashboard()
    elif page == "Team":
        team()
    elif page == "Feedback":
        feedback()
