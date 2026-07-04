#!/bin/bash

# Move to the directory where this script is located
cd "$(dirname "$0")"

# Activate the Python virtual environment
source .venv/bin/activate

# Launch the Streamlit application
streamlit run rag_app/app.py
