import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


async def call_ai(prompt: str, system: str | None = None):
    """
    Chama o provedor de IA de forma síncrona numa thread e retorna o texto.

    Implementa criação lazy do cliente OpenAI e fallback local quando
    não há chave de API ou quando a inicialização do cliente falha
    (útil para testes locais sem dependências externas).
    """

    def sync_call():
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        api_key = os.getenv("OPENAI_API_KEY")
        # Fallback de desenvolvimento — evita erro quando não há API key ou compatibilidade de libs
        if not api_key:
            return (
                "[MOCK OPENAI RESPONSE]\n"
                "Nenhuma OPENAI_API_KEY encontrada — retornando resposta falsa para testes locais.\n\n"
                + prompt[:4000]
            )

        try:
            # import lazy para evitar efeitos colaterais em import time
            from openai import OpenAI

            client = OpenAI(api_key=api_key)
            resp = client.responses.create(
                model=MODEL,
                input=messages,
            )
            return resp.output_text
        except TypeError as e:
            # Compatibilidade de versões (openai/httpx) — cair para fallback de desenvolvimento
            return (
                "[MOCK OPENAI RESPONSE - falha ao inicializar cliente OpenAI]\n"
                f"Motivo: {e}\n\n"
                + prompt[:4000]
            )
        except Exception as e:
            return f"[Erro ao chamar OpenAI: {e}]"

    return await asyncio.to_thread(sync_call)
