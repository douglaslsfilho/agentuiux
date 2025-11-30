# main.py
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import asyncio

from app.agents.architecture_agent import ArchitectureAgent
from app.agents.documentation_agent import DocumentationAgent
from app.agents.uiux_agent import UIUXAgent
from app.agents.reviewer_agent import ReviewerAgent
from app.utils.document_reader import read_document_filebytes

app = FastAPI(title="Agent Frontend Orchestrator - UX Pipeline")

# Allow CORS if needed (ajuste origins conforme necessário)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

architecture_agent = ArchitectureAgent()
documentation_agent = DocumentationAgent()
uiux_agent = UIUXAgent()
reviewer_agent = ReviewerAgent()

def logger(msg: str):
    print(msg)


@app.post("/generate")
async def generate(
    backlog: str = Form(...),
    file: UploadFile | None = File(None)
):
    """
    Endpoint que aceita:
    - backlog (string, campo Form)
    - file (opcional) -> pdf/docx/txt
    Retorna a pipeline completa (architecture, documentation, uiux_analysis, review).
    """
    task_id = "TASK_001"

    # extrair texto do arquivo, se enviado
    documents_text = ""
    if file:
        file_bytes = await file.read()
        documents_text = await read_document_filebytes(file_bytes, file.filename)

    try:
        # 1) Arquitetura
        arch_result = await architecture_agent.run({"backlog": backlog}, logger, task_id)
        architecture = arch_result.get("frontend_architecture", "")

        # 2) Documentação
        doc_result = await documentation_agent.run(
            {"backlog": backlog, "architecture": architecture},
            logger,
            task_id
        )
        documentation = doc_result.get("documentation", "")

        # 3) UI/UX (agora recebe documents)
        uiux_result = await uiux_agent.run(
            {
                "backlog": backlog,
                "architecture": architecture,
                "documents": documents_text
            },
            logger,
            task_id
        )
        uiux_analysis = uiux_result.get("uiux_analysis", "")

        # 4) Review
        review_result = await reviewer_agent.run(
            {
                "backlog": backlog,
                "architecture": architecture,
                "documentation": documentation
            },
            logger,
            task_id
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
