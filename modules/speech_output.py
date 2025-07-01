import pyttsx3

def init_engine():
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    engine.setProperty('volume', 1)
    return engine

def list_voices(engine):
    voices = engine.getProperty('voices')
    for index, voice in enumerate(voices):
        print(f"Voice {index}: {voice.name} - {voice.id}")
    return voices

def speak_message(engine, message, voice_index=0):
    voices = list_voices(engine)
    engine.setProperty('voice', voices[voice_index].id)
    engine.say(message)
    engine.runAndWait()