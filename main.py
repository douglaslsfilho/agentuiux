from fastapi import FastAPI, HTTPException
from app.agents.architecture_agent import ArchitectureAgent
from app.agents.documentation_agent import DocumentationAgent
from app.agents.uiux_agent import UIUXAgent
from app.agents.reviewer_agent import ReviewerAgent

app = FastAPI(title="Frontend Intelligence Agent")

# instanciando os agentes
architecture_agent = ArchitectureAgent()
documentation_agent = DocumentationAgent()
uiux_agent = UIUXAgent()
reviewer_agent = ReviewerAgent()


def logger(msg: str):
    """Logger simples para exibir mensagens no terminal."""
    print(msg)


@app.post("/generate")
async def generate(payload: dict):
    """
    Executa toda a pipeline de geração:
    1. Arquitetura
    2. Documentação
    3. UI/UX
    4. Revisão final
    """
    task_id = "TASK_001"

    try:
        # 1️⃣ Arquitetura
        arch_result = await architecture_agent.run(payload, logger, task_id)
        architecture = arch_result.get("frontend_architecture", "")

        # 2️⃣ Documentação
        doc_result = await documentation_agent.run(
            {**payload, "architecture": architecture}, logger, task_id
        )
        documentation = doc_result.get("documentation", "")

        # 3️⃣ UI/UX
        uiux_result = await uiux_agent.run(
            {**payload, "architecture": architecture}, logger, task_id
        )
        uiux_analysis = uiux_result.get("uiux_analysis", "")

        # 4️⃣ Revisão final
        review_result = await reviewer_agent.run(
            {
                **payload,
                "architecture": architecture,
                "documentation": documentation,
            },
            logger,
            task_id,
        )
        review = review_result.get("review", "")

        return {
            "architecture": architecture,
            "documentation": documentation,
            "uiux_analysis": uiux_analysis,
            "review": review,
        }

    except Exception as e:
        logger(f"[{task_id}] Erro: {e}")
        raise HTTPException(status_code=500, detail=str(e))
