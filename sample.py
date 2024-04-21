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

# Title
st.title("Hello GeeksForGeeks !!!")

 
# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
n1 = st.text_input("Enter First Number")
n2 = st.text_input("Enter Second Number")
n3 = st.text_input("Enter Third Number")
    
# .title() is used to get the input text string
if(st.button('Submit')):    
    result = largest(n1, n2, n3)
    st.success(result)
