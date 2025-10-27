import streamlit as st
import fitz  # PyMuPDF for PDF text extraction

def extract_text_from_pdf(pdf_file):
    """Extract text from each page of the PDF."""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    pages_text = []
    for i, page in enumerate(doc):
        text = page.get_text("text")
        pages_text.append((i + 1, text))
    return pages_text

# --- Streamlit app ---
st.title("🔎 PDF Search Tool")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    st.success("✅ PDF uploaded successfully!")

    query = st.text_input("Enter your search term")

    if query:
        pdf_text = extract_text_from_pdf(uploaded_file)
        results = []

        for page_num, text in pdf_text:
            if query.lower() in text.lower():
                # grab snippet around the query
                start = text.lower().index(query.lower())
                snippet = text[max(0, start-50): start+100]
                results.append((page_num, snippet))

        if results:
            st.write(f"### Found {len(results)} matches:")
            for page, snippet in results:
                st.markdown(f"**Page {page}:** ...{snippet}...")
        else:
            st.warning("No matches found.")
