#!/bin/bash

# Audio Analysis Script Runner
# This script ensures you're in the right directory and using the right Python

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Change to the script directory
cd "$SCRIPT_DIR"

# Check if audio file is provided
if [ $# -eq 0 ]; then
    echo "Usage: ./analyze_audio.sh <audio_file_path>"
    echo "Example: ./analyze_audio.sh sound.mp3"
    echo "Example: ./analyze_audio.sh sound_short.mp3"
    exit 1
fi

AUDIO_FILE="$1"

# Check if audio file exists
if [ ! -f "$AUDIO_FILE" ]; then
    echo "Error: Audio file not found at '$AUDIO_FILE'"
    echo "Make sure the file path is correct and the file exists."
    exit 1
fi

echo "🎵 Running audio analysis..."
echo "📁 Working directory: $(pwd)"
echo "🎵 Audio file: $AUDIO_FILE"
echo "🐍 Python: $(which python3)"
echo ""

# Try different Python installations
echo "🔍 Trying different Python installations..."

# Try system Python first (where we just installed librosa)
if /Library/Frameworks/Python.framework/Versions/3.11/bin/python3 -c "import librosa" 2>/dev/null; then
    echo "✅ Using system Python with librosa"
    /Library/Frameworks/Python.framework/Versions/3.11/bin/python3 analyze_audio.py "$AUDIO_FILE"
elif python3 -c "import librosa" 2>/dev/null; then
    echo "✅ Using default python3 with librosa"
    python3 analyze_audio.py "$AUDIO_FILE"
else
    echo "❌ No Python installation found with librosa"
    echo "Please install librosa:"
    echo "  /Library/Frameworks/Python.framework/Versions/3.11/bin/python3 -m pip install librosa"
    echo "  or"
    echo "  python3 -m pip install librosa"
    exit 1
fi

echo ""
echo "✅ Analysis complete! Check the generated files:"
echo "   - audio-analysis.js (for your website)"
echo "   - audio_analysis.json (raw data)"
