from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the API key
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

# Define the model and chat session
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="""You are SAI (Shubham's Artificial Intelligence). You're my personal chatbot. You'll refer me by my name. My full name is Shubham Kumar. My USN(university seat number) is 1AM21CS186. I am pursuing my bachelors in Engineering (Computer Science). I am currently in my 5th Semester of Graduate Degree. I am currently in AMC Engineering College, Bangalore. I am 22 years old. Refer to me as Shubham.

July 2024 Examination Score (Semester 4 Result):

Subject Code, Subject Name, Internal Marks, External Marks, Total, Result, Annouced/ Updated on

BCS401, Analysis & Design of Algorithms, 23, 13, 36, F, 2024-09-20
BCS402, Microcontrollers, 32, 7, 39, F, 2024-09-20
BCS403, DBMS, 30, 18, 48, P, 2024-09-20
BCSL404, ADA LAB, 36,31,67,P,2024-09-20
BBPC407, Biology for Computer Engineers, 32,21,53,P,2024-09-20
BUHK408, Universal Human Values Course, 44, 24, 68, P, 2024-09-20
BPEK459, Physical Education, 99, 0, 99,P, 2024-09-20
BCS405A, Discrete Mathematical Structures, 23,10,33,F,2024-09-20
BCS456B, Capacity Planning for IT,24,22,46,P,2024-09-20


Semester 2 Result:

Subject Code, Subject Name, Internal Marks, External Marks, Total, Result, Annouced/ Updated on

BMATS201, Mathematics-II for CSE Stream, 20, 13, 33, F, 2024-08-13


July 2023 Examination Score (Semester 2 Result):

Subject Code, Subject Name, Internal Marks, External Marks, Total, Result, Annouced/ Updated on

BMATS201, Mathematics-II for CSE Stream, 20, 13, 33, F, 2023-10-27
BCHES202, Applied Chemistry for CSE Stream, 20, 32, 52, P, 2023-10-27
BCEDK203, Computer Aided Engineering Drawing, 31,29,60,P, 2023-10-27
BPWSK206, Professional Writing Skills in English, 31,29,60,P,2023-10-27
BICOK207, Indian Constitution, 29, 21, 50, P,2023-10-27
BSFHK258, Scientific Foundation of Health, 30,33,63,P,2023-10-27
BPLCK205B, Introduction to python Programming, 30, 32, 62, P, 2023-10-27
BESCK204B, Introduction to electrical Engineering, 21,27,48,P,2023-10-27


Nomenclature/Abbreviations:

P-Pass, F- Fail, A-Absent, W-Withheld, X,NE- Not Eligible


    """
)

# Initialize the chat session
chat_session = model.start_chat(history=[])

# Set Streamlit page configuration
st.set_page_config(
    page_title="Shubham's Personal Chatbot 🤖",
    page_icon="🤖",
    layout="centered"
)

# Streamlit Interface
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.5em;
        color: #2A9D8F;
        font-weight: bold;
        text-align: center;
    }
    .subtitle {
        font-size: 1.2em;
        color: #FFFFFF;
        text-align: center;
        margin-bottom: 20px;
    }
    .response-box {
        background-color: #1E1E1E;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #2A9D8F;
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown('<h1 class="main-title">Shubham\'s Personal Chatbot 🤖</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Ask me anything, and I\'ll assist you to the best of my ability!</p>', unsafe_allow_html=True)

# Input from the user
st.markdown("### 💬 Enter your question below:")
user_input = st.text_input("Type your question:", "")

# Chat session and response display
if st.button("Send"):
    if user_input.strip():
        with st.spinner("🤔 SAI is thinking..."):
            try:
                response = chat_session.send_message(user_input)
                st.markdown("### 🤖 Response:")
                st.markdown(
                    f'<div class="response-box">{response.text}</div>',
                    unsafe_allow_html=True,
                )
            except Exception as e:
                st.error(f"❌ An error occurred: {e}")
    else:
        st.error("⚠️ Please enter a valid question!")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; font-size: 0.9em; color: #7D7D7D;">
        Created with ❤️ by Shubham Kumar | Powered by Gemini AI
    </div>
    """,
    unsafe_allow_html=True,
)
