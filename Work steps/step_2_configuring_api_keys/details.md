# Step 2: Configuring Google Cloud / Gemini API Keys safely

**Objective:** Ensure that our API keys are stored securely on the local machine and never accidentally leaked into version control.

### What we did
1. **Created a `.env` file**: This file acts as a local vault for environment variables. LangChain's Google integration automatically looks for the `GOOGLE_API_KEY` environment variable.
2. **Created a `.gitignore` file**: We explicitly told Git to ignore the `.env` file and our `.venv` folder, guaranteeing that sensitive keys or bulky dependency folders are never uploaded if you choose to push this project to GitHub.

### Files & Folders Created
- `.env` (File)
- `.gitignore` (File)
- `Work steps/step_2_configuring_api_keys/` (Folder)
- `Work steps/step_2_configuring_api_keys/details.md` (File)
