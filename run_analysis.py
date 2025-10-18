#!/usr/bin/env python3
"""
Audio Analysis Runner - Works with any Python installation
"""

import sys
import os
import subprocess

def find_python_with_librosa():
    """Find a Python installation that has librosa installed"""
    
    # List of possible Python paths to try
    python_paths = [
        "/Library/Frameworks/Python.framework/Versions/3.11/bin/python3",
        "/usr/bin/python3",
        "/usr/local/bin/python3",
        "python3",
        "python"
    ]
    
    for python_path in python_paths:
        try:
            # Test if this Python has librosa
            result = subprocess.run([
                python_path, "-c", "import librosa; print('librosa version:', librosa.__version__)"
            ], capture_output=True, text=True, timeout=10)
            
            if result.returncode == 0:
                print(f"✅ Found Python with librosa: {python_path}")
                print(f"   {result.stdout.strip()}")
                return python_path
                
        except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
            continue
    
    return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 run_analysis.py <audio_file_path>")
        print("Example: python3 run_analysis.py sound.mp3")
        print("Example: python3 run_analysis.py sound_short.mp3")
        sys.exit(1)
    
    audio_file = sys.argv[1]
    
    # Check if audio file exists
    if not os.path.exists(audio_file):
        print(f"❌ Error: Audio file not found at '{audio_file}'")
        print("Make sure the file path is correct and the file exists.")
        sys.exit(1)
    
    # Find Python with librosa
    python_path = find_python_with_librosa()
    
    if not python_path:
        print("❌ No Python installation found with librosa")
        print("\nTo fix this, install librosa in your Python environment:")
        print("  python3 -m pip install librosa")
        print("  or")
        print("  /Library/Frameworks/Python.framework/Versions/3.11/bin/python3 -m pip install librosa")
        sys.exit(1)
    
    # Run the analysis
    print(f"\n🎵 Running audio analysis with {python_path}...")
    print(f"📁 Audio file: {audio_file}")
    print("=" * 50)
    
    try:
        # Change to the script directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)
        
        # Run the analysis script
        result = subprocess.run([
            python_path, "analyze_audio.py", audio_file
        ], cwd=script_dir)
        
        if result.returncode == 0:
            print("\n✅ Analysis complete! Check the generated files:")
            print("   - audio-analysis.js (for your website)")
            print("   - audio_analysis.json (raw data)")
        else:
            print(f"\n❌ Analysis failed with exit code {result.returncode}")
            sys.exit(1)
            
    except Exception as e:
        print(f"\n❌ Error running analysis: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
