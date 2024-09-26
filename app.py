#!/usr/bin/env python3
import streamlit as st
from login import login_page
from dashboard import dashboard_logic

# Setting page config
st.set_page_config(page_title="BootBuddy", page_icon="🧑‍💻", layout="wide")

# Simulating a simple login system
def login(username, password):
    if username == 'admin' and password == 'password':  # Basic example credentials
        st.session_state.logged_in = True
        return True
    return False

# Create session state for user authentication
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Logout function
def logout():
    st.session_state.logged_in = False

# Main application logic
def main():
    st.header("BootBuddy Web App")

    # User is logged in
    if st.session_state.logged_in:
        dashboard_logic()
        if st.sidebar.button("Logout"):
            logout()
            st.experimental_rerun()
    else:
        username, password = login_page()
        
        if st.button("Login"):
            if login(username, password):
                st.success("Logged in successfully!")
                st.experimental_rerun()
            else:
                st.error("Invalid username or password")


if __name__ == "__main__":
    main()
