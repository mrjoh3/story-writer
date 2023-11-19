# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

audio_file= open("/home/matt/Music/Odin_recording/230822_0075.MP3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

