from ..provider import call_ai

class UIUXAgent:
    name = "UIUXAgent"

    async def run(self, payload: dict, logger, task_id: str, provider=None):
        logger(f"[{task_id}] [{self.name}] Iniciando análise de UI/UX...")

        backlog = payload.get("backlog", "")
        architecture = payload.get("architecture", "")

        prompt = (
            "Você é um especialista sênior em UI e UX. "
            "Com base no backlog e na arquitetura do projeto, analise e recomende melhorias na interface e na experiência do usuário. "
            "Considere:\n\n"
            "• Hierarquia visual e clareza na navegação;\n"
            "• Acessibilidade (contraste, legibilidade, tamanhos, uso de ARIA);\n"
            "• Consistência de design (cores, tipografia, espaçamento, ícones);\n"
            "• Feedback visual e microinterações (carregamento, erros, confirmações);\n"
            "• Usabilidade em dispositivos móveis e responsividade;\n"
            "• Estrutura dos componentes de interface (layout, grids, navegação lateral/superior);\n"
            "• Sugestões de melhorias com exemplos práticos (em texto ou pseudo-código CSS/HTML se necessário);\n"
            "• Ferramentas recomendadas (Figma, Storybook, Tailwind, Chakra UI, etc.) e justificativas.\n\n"
            f"ARQUITETURA:\n{architecture}\n\n"
            f"BACKLOG:\n{backlog}\n\n"
            "Retorne um relatório em Markdown com seções organizadas por tópico, destacando pontos fortes e sugestões de melhoria."
        )

        uiux_report = await call_ai(prompt)
        logger(f"[{task_id}] [{self.name}] Relatório de UI/UX gerado com sucesso.")

        return {"uiux_analysis": uiux_report}
