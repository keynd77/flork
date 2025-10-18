# Audio Analysis Script

## Usage

The `analyze_audio.py` script analyzes audio files and automatically generates comprehensive beat detection data for your audio-reactive website.

### Method 1: Python Runner (Recommended)

Use the Python runner that automatically finds the right Python installation:

```bash
python3 run_analysis.py <audio_file_path>
```

### Method 2: Shell Script

Use the shell script for guaranteed compatibility:

```bash
./analyze_audio.sh <audio_file_path>
```

### Method 3: Direct Python

```bash
python3 analyze_audio.py <audio_file_path>
```

### Examples

```bash
# Using Python runner (recommended - works with any Python)
python3 run_analysis.py sound.mp3
python3 run_analysis.py sound_short.mp3
python3 run_analysis.py my_music.wav

# Using shell script
./analyze_audio.sh sound.mp3
./analyze_audio.sh sound_short.mp3
./analyze_audio.sh my_music.wav

# Using Python directly
python3 analyze_audio.py sound.mp3
python3 analyze_audio.py sound_short.mp3
python3 analyze_audio.py my_music.wav
```

### What it does

1. **Analyzes the audio file** using librosa for comprehensive beat detection
2. **Automatically generates** `audio-analysis.js` with timing data
3. **Automatically generates** `audio_analysis.json` with raw analysis data
4. **Updates the HTML file** to use the new audio file automatically
5. **Updates your website** - just refresh the page to use the new analysis!

### Output Files

- **`audio-analysis.js`** - JavaScript file with timing map and audio state functions (used by your website)
- **`audio_analysis.json`** - Raw analysis data in JSON format (for reference)

### Requirements

Make sure you have librosa installed:
```bash
pip install librosa
```

### Features

- **Beat Detection** - Finds all beats and their intensities
- **Tempo Analysis** - Tracks BPM changes throughout the track
- **Rhythm Analysis** - Analyzes rhythm consistency and speed variations
- **Energy Analysis** - Detects energy peaks and intensity changes
- **Spectral Analysis** - Analyzes frequency content and brightness

The script automatically integrates with your existing website - no manual copying needed!
