import re
import requests

def extract_and_clean_inner_lists(text):
    result = []  # Final list to store cleaned content
    temp = ""    # Temporary string to collect characters
    depth = 0    # Track nesting level

    for char in text:
        if char == "[":
            depth += 1  # Increase depth on encountering '['
            if depth == 2:  # Start collecting at second level
                temp = ""  # Reset temp for a new inner list
        elif char == "]":
            if depth == 2:  # When closing an inner list
                cleaned_content = clean_text(temp)
                result.append(cleaned_content)  # Add cleaned content to the list
            depth -= 1  # Decrease depth on encountering ']'
        elif depth == 2:
            temp += char  # Collect content only inside second-level brackets

    return result

def clean_text(text):
    # Step 1: Remove all newline characters (\n)
    text = text.replace('\n', ' ')

    # Step 2: Remove unwanted characters like \, /, ", and extra spaces
    return re.sub(r'[\\/"\n]', '', text).strip()

def text_to_speech(api_key, text, output_path):
    voice_id='29vD33N1CtxCmqQRPOHJ'
    """
    Converts text to speech using the ElevenLabs API and saves it as an audio file.

    Parameters:
        api_key (str): Your ElevenLabs API key.
        text (str): The text you want to convert to speech.
        voice_id (str): The ID of the voice to use.
        output_path (str): The path where the audio file will be saved (including filename).
    """
    
    # Set up the request headers
    headers = {
        "accept": "audio/mpeg",
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }

    # Set up the JSON payload
    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    # Make the request to ElevenLabs API
    response = requests.post(f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}", 
                             json=payload, headers=headers)

    # Save the audio file if the response is successful
    if response.status_code == 200:
        with open(output_path, "wb") as audio_file:
            audio_file.write(response.content)
        print(f"Audio saved as {output_path}")
    else:
        print(f"Failed to generate speech: {response.status_code} - {response.text}")



