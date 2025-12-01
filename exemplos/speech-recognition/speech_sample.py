import azure.cognitiveservices.speech as speechsdk

speech_key = "SUA_CHAVE"
service_region = "REGIAO"

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
audio_config = speechsdk.audio.AudioConfig(filename="audio.wav")
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

result = speech_recognizer.recognize_once()
print("Texto transcrito:", result.text)