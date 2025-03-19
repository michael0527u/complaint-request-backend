import httpx
from app.core.config import settings

async def generate_letter(prompt: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            settings.OPENROUTER_BASE_URL,
            headers={"Authorization": f"Bearer {settings.OPENROUTER_API_KEY}"},
            json={"model": "anthropic/claude-3.5-haiku", "messages": [{"role": "user", "content": prompt}]}
        )
        return response.json()["choices"][0]["message"]["content"]
