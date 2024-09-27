#!/usr/bin/env python3
import streamlit as st

def authenticate(username, password):
    if username == "admin" and password == "password":  # Hardcoded credentials for testing
        return True
    return False

def show_login_page():
    # Custom CSS for centering content and styling the Streamlit button
    st.markdown("""
        <style>
        .center-logo {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
        .styled-button-container {
            display: flex;
            justify-content: center;
            margin-bottom: 15px;
        }
        div.stButton > button {
            background-color: #0097b2;
            color: white;
            padding: 10px 40px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            width: 200px;
        }
        div.stButton > button:hover {
            background-color: #007a94;
        }
        </style>
        """, unsafe_allow_html=True)

    # Logo and title
    st.markdown('<div class="center-logo"><img src="https://i.ibb.co/Q7BsbYW/bootbuddy-logo.png" width="150"></div>', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>Welcome to BootBuddy!</h1>", unsafe_allow_html=True)

    # Username and Password inputs
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Centering the button and using the real Streamlit button for functionality
    st.markdown('<div class="styled-button-container">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 3])
    with col1:
        st.write("") 
    with col2:
        login_button = st.button("Login")  # Handles the login click event
    with col3:
        signup_button = st.button("Sign Up") # # Handles the signup click event
    # Close the button container div
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Handle the button logic after click
    if login_button:
        if authenticate(username, password):
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")

    if signup_button:
        st.info("Sign up page coming soon!")  # Placeholder for signup action
