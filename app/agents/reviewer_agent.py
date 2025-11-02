from ..provider import call_ai

class ReviewerAgent:
    name = "ReviewerAgent"

    async def run(self, payload: dict, logger, task_id: str, provider=None):
        logger(f"[{task_id}] [{self.name}] Iniciando revisão final...")
        backlog = payload.get("backlog", "")
        architecture = payload.get("architecture", "")
        documentation = payload.get("documentation", "")
        prompt = (
            "Você é um revisor sênior. Revise a consistência entre backlog, arquitetura e documentação. "
            "1) Aponte 5 melhorias priorizadas (rápidas e de alto impacto). "
            "2) Identifique inconsistências. "
            "3) Sugira um checklist de 5 passos para validar a arquitetura durante as primeiras sprints.\n\n"
            f"BACKLOG:\n{backlog}\n\nARQUITETURA:\n{architecture}\n\nDOCUMENTAÇÃO:\n{documentation}"
        )
        review = await call_ai(prompt)
        logger(f"[{task_id}] [{self.name}] Revisão concluída.")
        return {"review": review}
