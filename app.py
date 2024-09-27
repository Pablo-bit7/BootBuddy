#!/usr/bin/env python3
import streamlit as st
from login import show_login_page

# Set page configuration
st.set_page_config(page_title="BootBuddy", page_icon="🧑‍💻", layout="centered")

# Main app logic
def main():
    show_login_page()


if __name__ == "__main__":
    main()
