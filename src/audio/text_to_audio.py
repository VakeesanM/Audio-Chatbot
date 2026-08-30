import pyttsx3


def intilize_engine():
    engine = pyttsx3.init()
    # Changing the Voice

    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)

    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)


    return engine

def speak(engine, text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    audio_engine = intilize_engine()
    speak(audio_engine, "This is a test!")

    