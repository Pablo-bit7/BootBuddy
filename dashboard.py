#!/usr/bin/env python3
import streamlit as st


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
    # Navigation definition
    page = st.navigation([
        st.Page(dashboard, title="Dashboard", icon="🏠"),
        st.Page(team, title="Team", icon="👥"),
        st.Page(feedback, title="Feedback", icon="💬"),
    ])
    page.run() # Run the selected page

    # Logout button styled separately
    if st.sidebar.button("Logout"):
        st.session_state.clear()
        st.rerun()  # Refresh to return to the login page

