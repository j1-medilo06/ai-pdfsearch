# Install Streamlit and PyMuPDF via Homebrew (optional global install)
brew install streamlit pymupdf

# Install Streamlabs OBS (if needed for streaming/demo purposes)
brew install --cask streamlabs

# Create a new virtual environment (recommended)
python3 -m venv path/to/venv

# Activate the virtual environment
source path/to/venv/bin/activate

# Install Project Dependencies
python3 -m pip install streamlit

#Re-activates your virtual environment (in case it was deactivated or your terminal was restarted) to ensure further installations occur inside the same environment.
source path/to/venv/bin/activate

# Install PyMuPDF
pip install PyMuPDF

# Launches your Streamlit web application (code.py).
# Streamlit will automatically open a local web server (default: http://localhost:8501
# ) where you can interact with your app in a browser.
streamlit run code.py 
