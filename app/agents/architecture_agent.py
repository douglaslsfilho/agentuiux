from ..provider import call_ai

class ArchitectureAgent:
    name = "FrontendArchitectureAgent"

    async def run(self, payload: dict, logger, task_id: str, provider=None):
        logger(f"[{task_id}] [{self.name}] Definindo arquitetura do frontend...")

        backlog = payload.get("backlog", "")
        prompt = (
            "Você é um arquiteto especialista em FRONTEND. "
            "Com base neste backlog, descreva uma ARQUITETURA FRONTEND moderna, modular e escalável, "
            "detalhando:\n\n"
            "• Frameworks ou bibliotecas recomendadas (React, Next.js, Vue, Angular, etc.) e a justificativa da escolha;\n"
            "• Estrutura de pastas e organização de componentes (pages, components, hooks, context, styles...);\n"
            "• Estratégia de roteamento e gerenciamento de estado (React Router, Zustand, Redux, Context API...);\n"
            "• Padrões de comunicação com APIs e serviços (REST, GraphQL, fetch hooks, axios, etc.);\n"
            "• Boas práticas de acessibilidade (A11y), responsividade e design system;\n"
            "• Estratégias de performance (lazy loading, memoização, otimização de assets, caching, code splitting...);\n"
            "• Sugestão de ferramentas de build e testes (Vite, Webpack, Jest, Testing Library...);\n"
            "• Principais riscos ou pontos de atenção relacionados à manutenção e escalabilidade do frontend.\n\n"
            f"BACKLOG:\n{backlog}\n\n"
            "Retorne um resumo estruturado em Markdown, com seções claras para cada tópico."
        )

        architecture = await call_ai(prompt)
        logger(f"[{task_id}] [{self.name}] Arquitetura de frontend gerada com sucesso.")
        return {"frontend_architecture": architecture}
