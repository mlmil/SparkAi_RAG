#!/bin/zsh -il

# Move to the directory where this script is located
cd "$(dirname "$0")"

echo "Building Project Knowledge Graph..."

# Launch the Antigravity CLI and ask it to build the initial graph
agy "/graphify ."
