from ..provider import call_ai

class BacklogAgent:
    name = "BacklogAgent"

    async def run(self, payload: dict, logger, task_id: str, provider=None):
        logger(f"[{task_id}] [{self.name}] Iniciando geração do backlog...")
        desc = payload.get("description", "")
        prompt = (
            "Você é um especialista em Product Management.\n\n"
            "Com base nesta descrição do projeto, gere uma lista priorizada de 6-12 itens "
            "de backlog (histórias/épicos), cada item com: título curto, descrição, "
            "prioridade (alta/média/baixa) e justificativa de valor de negócio.\n\n"
            f"DESCRIÇÃO:\n{desc}\n\nRETORNE EM JSON LISTA."
        )
        backlog_text = await call_ai(prompt)
        logger(f"[{task_id}] [{self.name}] Backlog gerado.")
        return {"backlog": backlog_text}
