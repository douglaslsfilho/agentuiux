from ..provider import call_ai

class UIUXAgent:
    name = "UIUXAgent"

    async def run(self, payload: dict, logger, task_id: str, provider=None):
        logger(f"[{task_id}] [{self.name}] Iniciando análise UX/UI e Acessibilidade...")

        backlog = payload.get("backlog", "")
        architecture = payload.get("architecture", "")
        documents = payload.get("documents", "")

        prompt = (
            "Você é um especialista sênior em UX/UI, Acessibilidade (WCAG 2.2), "
            "Pesquisa de Usuário e Heurísticas de Nielsen.\n\n"
            "Com base no BACKLOG, ARQUITETURA e DOCUMENTOS fornecidos, faça uma análise completa contendo:\n\n"

            "🔵 **1. Acessibilidade (WCAG 2.1 / 2.2)**\n"
            "• Contraste, tipografia e legibilidade.\n"
            "• Navegação por teclado e leitores de tela.\n"
            "• ARIA roles e semântica.\n"
            "• Erros comuns que prejudicam PCDs.\n\n"

            "🟢 **2. Pesquisa de Usuário (UX Research)**\n"
            "• Defina possíveis usuários-alvo.\n"
            "• Gere 1 a 2 personas baseadas no backlog.\n"
            "• Sugira métodos de pesquisa adequados (entrevista, survey, card sorting, teste moderado...).\n"
            "• Liste perguntas úteis para entrevistas.\n"
            "• Forme hipóteses de comportamento.\n\n"

            "🟣 **3. Heurísticas de Nielsen (Avaliação)**\n"
            "Avalie o sistema com base nas 10 heurísticas:\n"
            "• Visibilidade do estado do sistema\n"
            "• Controle e liberdade do usuário\n"
            "• Consistência\n"
            "• Prevenção de erros\n"
            "• Reconhecimento vs memória...\n"
            "E aponte riscos e melhorias.\n\n"

            "🟡 **4. Jornada do Usuário (User Journey)**\n"
            "• Principais etapas da jornada.\n"
            "• Atritos (pain points).\n"
            "• Oportunidades de melhoria.\n\n"

            "🟠 **5. Recomendações UI práticas**\n"
            "• Organização visual.\n"
            "• Hierarquia e navegação.\n"
            "• Boas práticas de layout, mobile-first.\n"
            "• Exemplos práticos (pode usar pseudo HTML/CSS sem exagerar).\n\n"

            "🟤 **6. Plano de Teste de Usabilidade**\n"
            "• Cenários.\n"
            "• Tarefas.\n"
            "• Métricas (SUS, tempo de tarefa, taxa de sucesso).\n"
            "• Critérios mínimos de aceitação.\n\n"

            "Retorne tudo em **Markdown organizado com seções claras**.\n\n"
            f"BACKLOG:\n{backlog}\n\n"
            f"ARQUITETURA:\n{architecture}\n\n"
            f"DOCUMENTOS (PDF/TXT/DOCX):\n{documents}\n\n"
        )

        result = await call_ai(prompt)
        logger(f"[{task_id}] [{self.name}] Relatório UX/UI/Acessibilidade gerado com sucesso.")

        return {"uiux_analysis": result}
