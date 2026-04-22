"""
Utility functions for the voice assistant.
"""

import os

from datetime import datetime
from settings import settings
from gtts import gTTS
from strands import tool

FILENAME = 'voz.mp3'


def speak(text: str):
    """Convert text to speech and play it."""
    tts = gTTS(text, lang=settings.LANGUAGE)
    tts.save(FILENAME)
    os.system(f'mpg123 -q {FILENAME}')  # ou vlc, ou ffplay
    os.remove(FILENAME)


@tool
def change_language_voice(language: str):
    """
    Change the language for text-to-speech.
    Args:
        language (str): The language code ('en' for English, 'pt' for Portuguese).
    """
    settings.LANGUAGE = language
    return f'Language changed to {language}'


@tool
def get_user_current_day_time():
    """
    Returns the current date and time.

    Use this tool whenever the user asks for current time or date.
    """
    now = datetime.now()

    return {
        'current_datetime': now.strftime('%d-%m-%Y|%H:%M:%S'),
        'date': now.strftime('%d-%m-%Y'),
        'time': now.strftime('%H:%M:%S'),
    }
