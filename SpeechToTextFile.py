import speech_recognition as sr

r = sr.Recognizer()

# obtain audio from the microphone
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)

#audio from file
audiofile = sr.AudioFile("Soundaufnahmen/Aufnahme.wav")
with audiofile as source:
    audio = r.record(source)

returns = r.recognize_google(audio)

print(returns)
