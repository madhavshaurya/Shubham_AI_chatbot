import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
import requests

# Set Streamlit page configuration (MUST be the first Streamlit command)
st.set_page_config(
    page_title="Shubham's Personal Chatbot 🤖",
    page_icon="🤖",
    layout="wide"
)

# Load environment variables
load_dotenv()

# Configure the API keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "your_gemini_api_key_here")
UNSPLASH_API_KEY = os.getenv("UNSPLASH_API_KEY", "your_unspash_api_key_here")

if GEMINI_API_KEY == "your_gemini_api_key_here":
    st.warning("⚠️ Please replace 'your_gemini_api_key_here' with your actual Gemini API key.")
if UNSPLASH_API_KEY == "your_unspash_api_key_here":
    st.warning("⚠️ Please replace 'your_gemini_api_key_here' with your actual Gemini API key.")

genai.configure(api_key=GEMINI_API_KEY)

# Define the Gemini model and chat session
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
I belong from Bihar. 

I have completed my 10th and 12th from Delhi Public School, Patna.

My 10th Marks were as follows:- Physics-60
English-90
Maths-70
Biology-60
PE-60
My 12th Marks were:-
Maths-80
Physics-50
Chemistry-40

My Hobbies are playing Chess, Walking, Reading Books etc.

I currently do not have any technical skill which is of any use, Though I’m currently learning something which I don’t want to disclose.

My Father’s Name is Krishna Kumar Gupta.
My Mother’s Name is Rina Gupta.

Sgpa of 2nd semester is 7.1 
Sgpa of 4th semester is 7.5

    """
)

# Initialize the chat session
chat_session = model.start_chat(history=[])

# Chat history state
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Sidebar for chat history
st.sidebar.title("📜 Chat History")
if st.session_state["chat_history"]:
    for i, entry in enumerate(st.session_state["chat_history"]):
        with st.sidebar.expander(f"Chat {i+1}"):
            st.write(f"**User:** {entry['user']}")
            st.write(f"**SAI:** {entry['ai']}")
else:
    st.sidebar.info("No chat history available yet.")

# Clear chat history button
if st.sidebar.button("Clear Chat History"):
    st.session_state["chat_history"] = []
    st.sidebar.info("Chat history cleared.")

# Main content
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

st.markdown('<h1 class="main-title">Shubham\'s Personal Chatbot 🤖</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Ask me anything, or search for images!</p>', unsafe_allow_html=True)

# Input from the user
st.markdown("### 💬 Enter your question or image keyword below:")
user_input = st.text_input("Type your question or keyword:", "")

# Chat session and response display
if st.button("Send"):
    if user_input.strip():
        with st.spinner("🤔 SAI is thinking..."):
            try:
                response = chat_session.send_message(user_input)
                st.session_state["chat_history"].append({"user": user_input, "ai": response.text})
                st.markdown("### 🤖 Response:")
                st.markdown(
                    f'<div class="response-box">{response.text}</div>',
                    unsafe_allow_html=True,
                )
            except Exception as e:
                st.error(f"❌ An error occurred: {e}")
    else:
        st.error("⚠️ Please enter a valid question!")

# Unsplash image search
if st.button("Search Image"):
    if user_input.strip():
        with st.spinner("🔍 Searching Unsplash..."):
            try:
                # Unsplash API call
                url = f"https://api.unsplash.com/search/photos"
                params = {
                    "query": user_input,
                    "client_id": UNSPLASH_API_KEY,
                    "per_page": 2,  # Fetch only 2 images
                }
                response = requests.get(url, params=params)
                if response.status_code == 200:
                    data = response.json()
                    images = data.get("results", [])
                    if images:
                        st.markdown("### 🖼️ Images:")
                        for img in images:
                            img_url = img["urls"]["small"]
                            st.image(img_url, use_column_width=True, caption=img.get("alt_description", "Image"))
                    else:
                        st.error("❌ No images found for your search.")
                else:
                    st.error(f"❌ Failed to fetch images. Error: {response.status_code}")
            except Exception as e:
                st.error(f"❌ An error occurred: {e}")
    else:
        st.error("⚠️ Please enter a valid keyword!")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; font-size: 0.9em; color: #7D7D7D;">
        Created with ❤️ by Shubham Kumar | Powered by Gemini AI & Unsplash
    </div>
    """,
    unsafe_allow_html=True,
)
