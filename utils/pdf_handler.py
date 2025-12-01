import fitz
def extract_text(file_path : str) -> str:
    content=[]
    with fitz.open(file_path) as docs:
        for page in docs:
            content.append(page.get_text())
    return "\n".join(content)