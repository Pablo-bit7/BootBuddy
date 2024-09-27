#!/usr/bin/env python3
import streamlit as st

# Sidebar Navigation
def sidebar_navigation():
    st.sidebar.title("Go to")
    selection = st.sidebar.radio(" ",["Dashboard", "Team", "Feedback"]) # Menu items

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
def show_dashboard():
    # Sidebar navigation
    page = sidebar_navigation()

    if page == "Dashboard":
        dashboard()
    elif page == "Team":
        team()
    elif page == "Feedback":
        feedback()

    # Add a logout button
    if st.button("Logout"):
        st.session_state['logged_in'] = False
        st.rerun()  # Refresh to return to the login page
