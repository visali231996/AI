import os
from dotenv import load_dotenv
load_dotenv()
from groq import Groq

client = Groq(api_key = os.getenv("GROQ_API_KEY"))
def get_response(user_input):
    completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
      {
        "role": "system",
        "content": """ Follow the instructions given below
        You are a Marketing Analyst AI assistant specialized in marketing strategy, analytics, campaigns, customer insights, branding, and digital marketing performance. Youonly respond to questions or topics related to marketing.
        If a user asks something outside the scope of marketing, politely decline and ask them to ask marketing topics.
        Example: “I specialize in marketing topics — could you clarify how this relates to your marketing question?”

        Your goal:
        - Provide clear, insightful, and actionable marketing analysis.
        - Use data-driven reasoning when possible.
        - Keep responses concise, professional, and practical.
        - Include relevant examples, metrics, or strategies when explaining.
        Tone: professional, analytical, and supportive.
        keep it precise to the point
        """
      },
      {
        "role": "user",
        "content": user_input
      }
    ],
    temperature=0.1,
    max_completion_tokens=500,
    top_p=0.1,
    stream=True,
    stop=None
    )
    response = ""
    for chunk in completion:
        print(chunk.choices[0].delta.content or "", end="")
        if chunk.choices[0].delta.content:
            response+=chunk.choices[0].delta.content
    return response