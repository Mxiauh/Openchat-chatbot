import PyPDF2
import io

def extract_text_from_pdf(pdf_file):
    """Extract text from an uploaded PDF file object."""
    text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Error extracting PDF: {e}")
    return text

def extract_text_from_txt(txt_file):
    """Extract text from an uploaded TXT file object."""
    try:
        # Read bytes and decode to string
        content = txt_file.getvalue().decode("utf-8")
        return content
    except Exception as e:
        print(f"Error extracting TXT: {e}")
        return ""

def process_document(uploaded_file):
    """
    Determine file type and extract text.
    Returns extracted text as a string.
    """
    if uploaded_file.name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".txt"):
        return extract_text_from_txt(uploaded_file)
    else:
        return ""

def augment_prompt(user_query, context):
    """
    Prepend the extracted document context to the user's query.
    """
    if not context:
        return user_query

    return (
        f"Use the following context to answer the question. "
        f"If the answer is not in the context, say you don't know based on the provided document.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {user_query}"
    )
