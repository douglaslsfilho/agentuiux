from ..provider import call_ai

class DocumentationAgent:
    name = "DocumentationAgent"

    async def run(self, payload: dict, logger, task_id: str, provider=None):
        logger(f"[{task_id}] [{self.name}] Gerando documentação explicativa...")
        architecture = payload.get("architecture", "")
        backlog = payload.get("backlog", "")
        prompt = (
            "Você é um technical writer que transforma arquitetura e backlog em documentação acessível.\n\n"
            "Gere um documento resumido (em Markdown) que contenha: visão geral do projeto, componentes-chave, "
            "fluxo de dados simplificado, mapa de funcionalidades (mapeando backlog para componentes), e instruções "
            "iniciais para começar o desenvolvimento (prioridade, sugestões de milestones).\n\n"
            f"ARQUITETURA:\n{architecture}\n\nBACKLOG:\n{backlog}\n\nRETORNE EM MARKDOWN."
        )
        documentation = await call_ai(prompt)
        logger(f"[{task_id}] [{self.name}] Documentação gerada.")
        return {"documentation": documentation}
