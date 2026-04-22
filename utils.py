"""
Utility functions for the voice assistant.
"""

import os

from gtts import gTTS

FILENAME = 'voz.mp3'


def speak(text: str):
    """Convert text to speech and play it."""
    tts = gTTS(text, lang='en')
    tts.save(FILENAME)
    os.system(f'mpg123 -q {FILENAME}')  # ou vlc, ou ffplay
    os.remove(FILENAME)
