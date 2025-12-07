Marketing Analyst Chatbot

A focused Marketing Analyst Chatbot powered by Groq LLM and built with Streamlit.
It provides only marketing-related guidance and remembers the last 5 messages for more contextual replies.

Features

Provides accurate marketing advice

Refuses to answer non-marketing topics (finance, health, business, etc.)

Remembers last 5 messages using Streamlit session state

Clean, interactive Streamlit UI

PDF export option for saving Q&A

Thread-based error handling

Can run both in terminal and UI mode

Project Structure
project/
│
├── agent.py        # Handles LLM calls using Groq API
├── chatbot.py      # Streamlit UI + session memory + PDF export
├── requirements.txt
└── README.md

agent.py

Calls the Groq LLM model using an API key

Collects and returns the model response

Ensures the chatbot answers only marketing-related questions

chatbot.py (Streamlit App)

Displays the chatbot UI

Stores the last 5 chat messages using st.session_state.history

Provides PDF export for questions and answers

Uses threads for error detection

Formats responses clearly

Output Behavior

The chatbot answers only marketing-related questions, including:

Market research

Branding

SEO/SEM

Customer segmentation

Product positioning

Social media strategy

Campaign analysis

It will not answer questions about:

Finance

Business operations

Health

Personal advice

Technology not related to marketing

Running the Application
Terminal Execution
python agent.py

Streamlit Interface
streamlit run chatbot.py

PDF Export

The Streamlit UI includes an option to download the conversation (questions and answers) as a PDF file.

Installation
Clone the repository
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

Install dependencies
pip install -r requirements.txt

Set your Groq API key
Windows (PowerShell)
setx GROQ_API_KEY "your_key_here"

macOS/Linux
export GROQ_API_KEY="your_key_here"

Tech Stack

Python 3.10+

Groq LLM API

Streamlit

ReportLab / FPDF for PDF generation

Threading for error handling
