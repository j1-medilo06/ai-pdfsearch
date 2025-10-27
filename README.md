🔎 PDF Search Tool
A simple Streamlit web app that allows you to search for specific keywords or phrases inside PDF files.
It uses PyMuPDF (fitz) for text extraction and Streamlit for an interactive, browser-based interface.

🧩 Features
📂 Upload any PDF file
🔍 Enter a search term to find all occurrences within the document
📄 Displays matching page numbers and text snippets around the search term
⚡ Runs locally with a minimal setup — no external API required

🛠️ Installation & Setup
1. (Optional) Install globally via Homebrew
```bash
brew install streamlit pymupdf
```

If you want to demo or record your Streamlit app:
```bash
brew install --cask streamlabs
```

2. Create a Virtual Environment (recommended)
```bash
python3 -m venv path/to/venv
```

3. Activate the Environment
```bash
source path/to/venv/bin/activate
```

4. Install Dependencies
```bash
pip install streamlit PyMuPDF
```

(You can also run python3 -m pip install streamlit first, then pip install PyMuPDF if you prefer step-by-step.)

🚀 Running the App
Once installed, start the Streamlit app:
```bash
streamlit run code.py
```

Streamlit will automatically launch your default web browser at:
```bash
http://localhost:8501

```
If it doesn’t open automatically, copy and paste the above URL into your browser.
