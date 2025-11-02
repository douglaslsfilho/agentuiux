import os
import asyncio
from dotenv import load_dotenv
from openai import OpenAI

# Carrega variáveis do arquivo .env
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

if not OPENAI_API_KEY:
    raise RuntimeError("Set OPENAI_API_KEY in environment (.env)")

# Cria o cliente da nova API
client = OpenAI(api_key=OPENAI_API_KEY)

# Função assíncrona para chamar o modelo
async def call_ai(prompt: str, system: str | None = None, max_tokens: int = 800):
    def sync_call():
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        # Nova forma de criar a requisição
        resp = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            max_tokens=max_tokens,
            temperature=0.2,
        )
        return resp.choices[0].message.content.strip()

    # Executa em thread separada para não travar o event loop
    return await asyncio.to_thread(sync_call)
