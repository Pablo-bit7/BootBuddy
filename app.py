#!/usr/bin/env python3
import streamlit as st
from login import show_login_page
from dashboard import show_dashboard


# Set page configuration
st.set_page_config(page_title="BootBuddy", page_icon="🧑‍💻", layout="centered") # Set page configuration

# Main app logic
def main():
    # Initialize session state for login status
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    # Check login status
    if st.session_state['logged_in']:
        show_dashboard()  # Show dashboard if logged in
    else:
        show_login_page()  # Show login page if not logged in


if __name__ == "__main__":
    main()
