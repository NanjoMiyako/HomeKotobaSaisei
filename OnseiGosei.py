"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech

import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './##GoogleのTextToSpeechの認証情報のjsonファイル##'



# Instantiates a client
client = texttospeech.TextToSpeechClient()

file_data = open("speechContent.txt", "r")
lines = []
count = 0
outputFileName = ""
str1 = "";

for line in file_data:
	lines.append(line)
	count = count + 1
	
	# Set the text input to be synthesized
	synthesis_input = texttospeech.types.SynthesisInput(text=line)

	# Build the voice request, select the language code ("en-US") and the ssml
	# voice gender ("neutral")
	voice = texttospeech.types.VoiceSelectionParams(
	    language_code='ja-JP',
	    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

	# Select the type of audio file you want returned
	audio_config = texttospeech.types.AudioConfig(
	    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

	outputFileName = "./output/output"
	outputFileName += str(count)
	outputFileName += ".mp3"

	# Perform the text-to-speech request on the text input with the selected
	# voice parameters and audio file type
	response = client.synthesize_speech(synthesis_input, voice, audio_config)

	# The response's audio_content is binary.
	with open(outputFileName, 'wb') as out:
	    # Write the response to the output file.
	    out.write(response.audio_content)
	    str1 = 'Audio content written to file "' + outputFileName + '"'
	    print(str1)
	    

file_data.close()