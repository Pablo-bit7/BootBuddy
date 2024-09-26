#!/usr/bin/env python3
import streamlit as st

def add_custom_css():
    st.markdown(
        """
        <style>
        body, .css-18e3th9, .css-1d391kg, .css-1cpxqw2 {
            background-color: white;
        }
        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            height: 100vh;
        }
        .stButton button {
            background-color: #0097b2;
            color: white;
            border-radius: 10px;
            width: 200px;
            height: 45px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def login_page():
    # Custom CSS for styling
    add_custom_css()
    
    # Centered Login Form
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    
    st.image("assets/bootbuddy_logo.png", width=200)  # Centered BootBuddy logo
    st.markdown("<h1 style='text-align: center;'>Login to BootBuddy</h1>", unsafe_allow_html=True)  # Centered login text
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    st.markdown('</div>', unsafe_allow_html=True)
    return username, password
