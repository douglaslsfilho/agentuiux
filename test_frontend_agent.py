import asyncio
from app.agents.architecture_agent import ArchitectureAgent

async def main():
    agent = ArchitectureAgent()

    payload = {
        "backlog": """
        - Tela inicial responsiva com menu lateral
        - Dashboard com gráficos interativos
        - Login com autenticação e recuperação de senha
        - Tema claro/escuro dinâmico
        - Formulário com validação em tempo real
        - Notificações e alertas visuais
        """
    }

    def logger(msg):
        print(msg)

    print("\n🚀 Executando FrontendArchitectureAgent...\n")
    result = await agent.run(payload, logger, "demo-task")
    print("\n✅ Resultado final:\n")
    print(result["frontend_architecture"])

if __name__ == "__main__":
    asyncio.run(main())
