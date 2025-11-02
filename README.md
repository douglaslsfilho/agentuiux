# MultiAgent Frontend - MVP (Backlog → Arquitetura → Documentação → Revisão)

## Requisitos
- Python 3.10+
- Conta OpenAI e chave de API

## Instalação
1. Crie virtualenv e ative:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate    # Windows
   ```
2. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure `.env`:
   - Copie `.env.example` para `.env` e coloque sua chave `OPENAI_API_KEY`.

## Estrutura
- `app/agents/`: contém cada agente (backlog, arquitetura, documentação, revisão)
- `app/provider.py`: comunica com a API OpenAI
- `examples/example_payload.json`: exemplo de entrada

## Uso
- Importe e execute cada agente dentro do seu orquestrador (Node.js, Python, etc.)
- Exemplo de uso rápido:
  ```python
  from app.agents.backlog_agent import BacklogAgent
  import asyncio
  async def main():
      payload = {"description": "App de IA para gestão de backlog"}
      def log(x): print(x)
      res = await BacklogAgent().run(payload, log, "demo")
      print(res)
  asyncio.run(main())
  ```
