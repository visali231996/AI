<b><u>#Marketing Analyst<\b><\u>
1. An chatbot which is used to provide focussed marketing advice on the user question.
2.uses memory to store last 5 messages so that it helps in delivering reliable outcomes.
3.Does not answer other than marketing issues.
4.uses streamlit as an UI interface to display the output in structured format. 
-------
<b><u>##Project Structure:<\b><\u>
###1.agent.py
uses groq api key to call llm model 
the obtained output is stored in response
###2.chatbot.py
uses streamlit to display the response in formatted UI
can be used to store messages in session_state.history
used to store last 5 messages
uses threads to detect any error
-------

<b><u>##output:<\b><\u>
answers to only marketing related questions.
strictly denied answering other questions related to finance,business,healthetc.,
----------
<b><u>##Running the application:<\b><\u>
<b><u>python agent.py<\b><\u>
gives the  response in the terminal
<b><u>streamlit run chatbot.py<\b><\u>
shows output in streamlit interface
----
also shows the pdf option in streamlit, where question and answers canbe stored in an pdf file.


