import asyncio
from app.agents.uiux_agent import UIUXAgent

# Simula um backlog e arquitetura simples
payload = {
    "backlog": "O usuário deve conseguir cadastrar e visualizar produtos no painel administrativo.",
    "architecture": "React + Vite + Zustand para estado global e TailwindCSS para estilização."
}

async def main():
    agent = UIUXAgent()
    result = await agent.run(payload, print, "TEST_UIUX")
    print("\n--- RESULTADO FINAL ---\n")
    print(result["uiux_analysis"])

asyncio.run(main())
