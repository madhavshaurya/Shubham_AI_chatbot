
# Shubham's Personal Chatbot 🤖

Shubham's Personal Chatbot is an AI-driven application that provides intelligent responses to your queries. The chatbot leverages Google Generative AI (Gemini) to deliver accurate and context-aware answers. Built with **Streamlit**, the interface is user-friendly and professional.

---

## Features

- **AI-Powered Responses**: Uses the Gemini AI model for advanced conversational capabilities.
- **Dark Mode Compatibility**: Designed for dark mode users for optimal visual experience.
- **Easy-to-Use Interface**: Clean and professional layout with emoji integration.

---

## Prerequisites

Before running the application, ensure you have the following installed:

1. **Python** (Version 3.8 or above)
2. **pip** (Python package manager)

---

## Installation Instructions

1. **Clone the Repository**  
   Clone this repository to your local machine using the following command:  
   ```bash
   git clone https://github.com/your-repo/shubham-chatbot.git
   cd shubham-chatbot
   ```

2. **Create a Virtual Environment** (Recommended)  
   ```bash
   python -m venv chatbot_env
   source chatbot_env/bin/activate  # For Linux/MacOS
   chatbot_env\Scripts\activate     # For Windows
   ```

3. **Install Required Modules**  
   Run the following command to install all necessary modules:  
   ```bash
   pip install -r requirements.txt
   ```

   Create a `requirements.txt` file (if not already included) with the following content:  
   ```plaintext
   streamlit
   google-generativeai
   python-dotenv
   ```

4. **Set Up Environment Variables**  
   Create a `.env` file in the root directory and add your API key:  
   ```plaintext
   GEMINI_API_KEY=your_google_api_key_here
   ```

---

## Running the Application

1. **Navigate to the Project Directory**  
   ```bash
   cd shubham-chatbot
   ```

2. **Start the Application**  
   Run the following command to start the Streamlit server:  
   ```bash
   streamlit run chatbot.py
   ```

3. **Access the Application**  
   Open the link provided in the terminal (typically `http://localhost:8501`) in your web browser.

---

## About Shubham's Chatbot

This chatbot is a personal assistant designed for Shubham Kumar. It is powered by the Gemini AI model and configured with a user-centric approach. The bot can:

- Respond to various queries with intelligence and context.
- Maintain a professional and interactive user experience.

### Technical Details

- **Frontend**: Built using Streamlit for a responsive web interface.
- **Backend**: Uses the Gemini AI model for generating text-based responses.
- **Customization**: Preloaded with Shubham's personalized details and instructions.

---

## Troubleshooting

- **Error: API Key Missing**  
  Ensure your `.env` file contains the correct API key.  
  ```plaintext
  GEMINI_API_KEY=your_google_api_key_here
  ```
- **Modules Not Found**  
  Ensure you have installed all required modules with `pip install -r requirements.txt`.
- **App Not Launching**  
  Check if Python version is 3.8 or above and try reinstalling Streamlit.

---

## License

This project is for personal use and may not be redistributed without permission.

---

## Contact

If you have any questions or need support, feel free to contact **Shubham Kumar**.

#
