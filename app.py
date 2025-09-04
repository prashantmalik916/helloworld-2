from src.add import addition
from src.subtract import subtraction
import streamlit as st

st.title("Calculator")


a = st.number_input("Enter the First Number : ", value=0)
b = st.number_input("Enter the Second Number : ", value=0)

option = st.selectbox(
    "Enter the Mathematical Operation you want to perform",
    ("Addition", "Subtraction"),
)

if st.button("Calculate"):
    if option == "Addition":
        result = addition(a, b)
    if option == "Subtraction":
        result == subtraction(a, b)
        
    st.write(f"Result : {result}")