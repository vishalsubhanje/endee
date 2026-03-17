from pypdf import PdfReader

def load_document(uploaded_file):
    file_name = uploaded_file.name.lower()

    if file_name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")

    elif file_name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
        return text

    else:
        return None