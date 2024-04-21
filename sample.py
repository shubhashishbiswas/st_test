# import module
import streamlit as st

def largest(n1, n2, n3):
    if n1 > n2 and n1 > n3: 
        return n1
    elif n2 > n1 and n2 > n3: 
        return n2
    elif n3 > n1 and n3 > n2: 
        return n3
    else:
        return "Error" 

 
n1 = st.text_input("Enter First Number")
n2 = st.text_input("Enter Second Number")
n3 = st.text_input("Enter Third Number")
    
if(st.button('Submit')):    
    result = largest(n1, n2, n3)
    st.success(result)
