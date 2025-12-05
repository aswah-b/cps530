import streamlit as st

st.set_page_config(page_title="CPS530 Lab 10 Problem 2", page_icon="🌐",layout="centered")

st.title("CPS530 Lab 10 Problem 2")
st.write("**Framework / Library used:** Streamlit (Python web-based framework)")

st.header("How I installed Streamlit")

st.markdown("""For this problem, I used streamlit, which is a Python based framework for building web applications.

**Steps I followed to install it:**

1. **Checking Python version**
   I made sure I had a recent version of Python 3 installed.

2. **Creating virtual environments**
   Used the command: pip install streamlit when the virtual environment was activated to install the streamlit package. 

3. **Installing Streamlit**
   I ran the command: pip install streamlit in my terminal to install the streamlit package and imported it in my python code.
            """)

st.subheader("Code used for this page/How I built this page with Streamlit")

st.markdown("""
Below is (almost) the same code that powers this page:
""")

code_example = '''import streamlit as st

st.set_page_config(page_title="CPS530 Lab 10 Problem 2",
page_icon="🌐",
layout="centered")

st.title("CPS530 Lab10 Problem 2")
st.write("Framework / Library used: Streamlit")
st.header("How I installed Streamlit")
st.markdown("[installation steps]")

st.header("How I built this page with Streamlit")
st.markdown("[code]")

st.header("Difficulties encountered and how I solved them")
st.markdown("[explanation]")
'''

st.code(code_example, language="python")

st.markdown("""
            as you can see, streamlit makes it very easy to create web pages using simple python code and markdown syntax found in their documentation.
            """)

st.header("3. Difficulties encountered and how I solved them")

st.markdown("""Streamlit is super simple and easy to use, but some difficulties I encountered were:
           
1. **Figuring out how to structure the page layout to make it visually appealing (I had to refer to the documentation and examples on the streamlit website).**
2. **Initally, I had the wrong python environment activated, so streamlit commands were not recognized. I solved this by ensuring I was in the correct virtual environment before running the streamlit app.**
3. **Understanding how to deploy the app for others to see. I researched deployment options and found that using streamlit cloud to host my streamlit app was the easiest method.**"""
)




