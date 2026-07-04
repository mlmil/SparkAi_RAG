#!/bin/zsh -il

# Move to the directory where this script is located
cd "$(dirname "$0")"

echo "Launching Antigravity Co-Pilot..."

# Launch the Antigravity CLI and immediately prompt it to read the local project memory
agy "I need help troubleshooting this RAG application. Please read AGENTS.md and AI_WORKLOG.md to get fully up to speed on the project state, then ask me what issues I am running into."
