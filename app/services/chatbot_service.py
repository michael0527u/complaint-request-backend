import openai
from app.core.config import settings


def generate_letter(user_name, register_number, subject, description):
    return f"""
From  
{user_name}  
{register_number}  
St. Joseph’s College of Engineering  
Chennai-600119  

To  
The Chairman  
St. Joseph’s College of Engineering  
Chennai-600119  

Respected Sir,  

Subject: {subject}  

{description}  

Thank you.  

Yours faithfully,  
{user_name}
"""


async def chat_with_ai(message: str):
    openai.api_key = settings.OPENROUTER_API_KEY
    response = openai.ChatCompletion.create(
        model="claude-3.5-haiku",
        messages=[{"role": "user", "content": message}]
    )
    return response["choices"][0]["message"]["content"]
