<b><u>Marketing Analyst Chatbot</u></b>

A focused marketing analyst chatbot powered by Groq LLM and built with Streamlit.
It provides only marketing-related guidance and remembers the last 5 messages for accurate contextual replies.
---------
<b><u> Features</u></b>

Provides focused marketing advice

Remembers the last 5 messages using Streamlit session state

Strictly refuses to answer non-marketing topics (finance, health, business, personal, etc.)

Streamlit UI for structured display

PDF export for saving question–answer sessions

Thread-based error detection and handling

<b><u>## Project Structure</u></b>
-----

project/
│
├── agent.py        # Handles Groq LLM calls
├── chatbot.py      # Streamlit UI, memory, PDF export
├── requirements.txt
└── README.md


<b><u>## 1. agent.py</u></b>

Uses Groq API key to call the LLM

Stores the obtained output as response

Ensures chatbot answers only marketing-related questions

<b><u>## 2. chatbot.py</u></b>

Uses Streamlit to display responses in a formatted UI

Stores chat messages in session_state.history

Retains only the last 5 messages

Uses threading to detect errors

Includes a PDF export option

<b><u>## Output</u></b>

✔ Answers to:

Marketing strategy

Market research

Social media marketing

Target audience analysis

Branding

Campaign suggestions

❌ Strictly refuses:

Finance

Health/medical

Business operations

Personal advice

Tech unrelated to marketing

<b><u>## Running the Application</u></b>

Terminal Output
python agent.py

Streamlit UI
streamlit run chatbot.py


This opens a Streamlit interface showing the output in a structured format.
Also includes a button to download the conversation as a PDF.

<b><u>## Installation</u></b>

Clone the repository
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

Install dependencies
pip install -r requirements.txt

Set Groq API Key
Windows:
setx GROQ_API_KEY "your_key_here"

macOS / Linux:
export GROQ_API_KEY="your_key_here"


<b><u>## Tech Stack</u></b>

Python 3.10+

Groq LLM

Streamlit

FPDF / ReportLab for PDF

Threading
