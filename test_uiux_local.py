# test_uiux_local.py
import asyncio
from app.agents.uiux_agent import UIUXAgent
from app.utils.document_reader import read_document_filebytes

async def main():
    # caminho do PDF local (se não existir, usa um fallback de texto)
    import os

    path = "sample.pdf"  # coloque um PDF de teste aqui
    if os.path.exists(path):
        with open(path, "rb") as f:
            b = f.read()
        filename = "sample.pdf"
    else:
        b = b"Documento de exemplo para testes locais.\nConteudo gerado localmente."
        filename = "sample.txt"

    text = await read_document_filebytes(b, filename)
    payload = {
        "backlog": "Usuário pode cadastrar e gerenciar produtos no painel admin.",
        "architecture": "React + Vite + Zustand + Tailwind",
        "documents": text
    }

    agent = UIUXAgent()
    res = await agent.run(payload, print, "TEST_UIUX")
    print("\n--- UI/UX ANALYSIS ---\n")
    print(res["uiux_analysis"][:4000])  # imprime os primeiros 4000 chars

asyncio.run(main())
