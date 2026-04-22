"""
Utility functions for the voice assistant.
"""

import os

from datetime import datetime
from settings import settings
from gtts import gTTS

FILENAME = 'voz.mp3'


def speak(text: str):
    """Convert text to speech and play it."""
    tts = gTTS(text, lang=settings.LANGUAGE)
    tts.save(FILENAME)
    os.system(f'mpg123 -q {FILENAME}')  # ou vlc, ou ffplay
    os.remove(FILENAME)


def change_language(language: str):
    """
    Change the language for text-to-speech.
    Args:
        language (str): The language code ('en' for English, 'pt' for Portuguese).
    """
    settings.LANGUAGE = language
    return f'Language changed to {language}'


def current_time():
    """Return the current time as a string."""
    now = datetime.now()
    return now.strftime('%H:%M:%S')
