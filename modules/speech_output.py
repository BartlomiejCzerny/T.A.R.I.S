import pyttsx3   # Import biblioteki do syntezy mowy (text-to-speech) działającej offline

def init_engine():
    # Inicjalizuj silnik mowy pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)   # Ustaw szybkość mówienia (słowa na minutę)
    engine.setProperty('volume', 1)   # Ustaw maksymalną głośność (1.0 = 100%)
    return engine                     # Zwróć skonfigurowany silnik

def list_voices(engine):
    # Pobierz dostępne głosy zainstalowane w systemie
    voices = engine.getProperty('voices')
    for index, voice in enumerate(voices):
        # Wypisz nazwę i identyfikator każdego głosu wraz z jego numerem
        print(f"Voice {index}: {voice.name} - {voice.id}")
    return voices   # Zwróć listę dostępnych głosów

def speak_message(engine, message, voice_index=0):
    # Pobierz i wypisz listę głosów
    voices = list_voices(engine)
    
    # Ustaw wybrany głos na podstawie indeksu (domyślnie pierwszy)
    engine.setProperty('voice', voices[voice_index].id)
    
    # Dodaj wiadomość do kolejki mówienia
    engine.say(message)

    # Rozpocznij syntezę mowy i poczekaj na zakończenie odczytu
    engine.runAndWait()