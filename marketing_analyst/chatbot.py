
import streamlit as st
import random
import time
from agent import get_response
from typing import List
from io import BytesIO
#from reportlab.lib.pagesizes import letter
#from reportlab.pdfgen import canvas
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


st.title("Marketing assistant")
    
# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)




# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history: List[str] = [] # type: ignore

def build_chat_template(history: List[str], latest_query: str, max_turns: int = 5) -> str:
    pruned = history[-max_turns:] if len(history) > max_turns else history
    prev = "\n".join(pruned) if pruned else "(none)"
    return f"Previous conversation: {prev}\nlatest query:{latest_query}"


    
    # ---- Show prior messages (best-effort split for display only) ----
for turn in st.session_state.history:
    # turn looks like: "User: ...\nAgent: ..."
    parts = turn.split("\nAgent:", 1)
    user_line = parts[0].removeprefix("User: ").strip()
    with st.chat_message("user"):
        st.markdown(user_line)
    if len(parts) == 2:
        agent_line = parts[1].strip()
        with st.chat_message("assistant"):
            st.markdown(agent_line)
    

    
if query := st.chat_input("How can I help you"):

    chat_template = build_chat_template(st.session_state.history, query, max_turns=5)
 
    try:

        response = get_response(chat_template)

    except Exception as e:

        response = f"[Error contacting model] {e}"
 
    with st.chat_message("user"):

        st.markdown(query)

    with st.chat_message("assistant"):

        st.markdown(response)
 
    st.session_state.history.append(f"User: {query}\nAgent: {response}")

    st.session_state.history = st.session_state.history[-5:]


st.title("🤖 Chatbot with PDF Export")

# --- Function to generate PDF from chat history ---
def create_pdf(history):
    pdf_buffer = BytesIO()
    pdf = canvas.Canvas(pdf_buffer, pagesize=letter)
    width, height = letter
    y = height - 50

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y, "Chat History")
    y -= 30
    pdf.setFont("Helvetica", 12)

    for turn in history:
        parts = turn.split("\nAgent:", 1)
        user_msg = parts[0].removeprefix("User: ").strip()
        agent_msg = parts[1].strip() if len(parts) > 1 else ""

        pdf.drawString(50, y, f"User: {user_msg}")
        y -= 20
        pdf.drawString(50, y, f"Agent: {agent_msg}")
        y -= 30

        # Add a new page if space runs out
        if y < 100:
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
            y = height - 50

    pdf.save()
    pdf_buffer.seek(0)
    return pdf_buffer

# --- Download PDF Button ---
if st.session_state.history:
    pdf_file = create_pdf(st.session_state.history)
    st.download_button(
        label="📄 Download Chat as PDF",
        data=pdf_file,
        file_name="chat_history.pdf",
        mime="application/pdf",
    )