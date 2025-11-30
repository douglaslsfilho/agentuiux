# app/utils/document_reader.py
import io

# carregamento defensivo de dependências opcionais
try:
    import PyPDF2
except Exception:
    PyPDF2 = None

try:
    import docx
except Exception:
    docx = None

async def read_document_filebytes(file_bytes: bytes, filename: str) -> str:
    """
    Recebe bytes do arquivo e o nome para decidir como extrair texto.
    Retorna string com o texto extraído.
    """
    fname = filename.lower()

    # TXT
    if fname.endswith(".txt"):
        try:
            return file_bytes.decode("utf-8")
        except UnicodeDecodeError:
            return file_bytes.decode("latin1", errors="ignore")

    # PDF
    if fname.endswith(".pdf"):
        text = ""
        try:
            if PyPDF2 is None:
                return "[PyPDF2 não instalado. Instale com: pip install PyPDF2]"

            reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        except Exception as e:
            return f"[Erro ao ler PDF: {e}]"
        return text.strip()

    # DOCX
    if fname.endswith(".docx"):
        try:
            if docx is None:
                return "[python-docx não instalado. Instale com: pip install python-docx]"

            doc = docx.Document(io.BytesIO(file_bytes))
            paragraphs = [p.text for p in doc.paragraphs if p.text and p.text.strip()]
            return "\n".join(paragraphs)
        except Exception as e:
            return f"[Erro ao ler DOCX: {e}]"

    return "[Formato não suportado. Suporte: .pdf, .docx, .txt]"
