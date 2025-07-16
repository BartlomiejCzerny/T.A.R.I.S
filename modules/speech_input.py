import speech_recognition as sr   # Import biblioteki do rozpoznawania mowy (speech-to-text)
from modules import speech_output   # Import modułu odpowiedzialnego za syntezę mowy (text-to-speech)

def recognize_speech_from_mic(timeout=5, phrase_time_limit=5):
    # Utwórz instancję rozpoznawacza mowy
    recognizer = sr.Recognizer()

    # Inicjalizuj silnik syntezy mowy (text-to-speech)
    engine = speech_output.init_engine()

    # Skorzystaj z domyślnego mikrofonu jako źródła dźwięku
    with sr.Microphone() as source:
        print("🎤 Słucham... Powiedz coś.")
        
        # Odtwórz przygotowaną wiadomość głosowo, korzystając z wybranego głosu (voice_index=0)
        speech_output.speak_message(engine, "Słucham... Powiedz coś.", voice_index=0)

        # Dostosuj się do szumów otoczenia, by poprawić dokładność rozpoznawania
        recognizer.adjust_for_ambient_noise(source)
        try:
            # Nasłuchuj wypowiedzi użytkownika przez określony czas
            audio = recognizer.listen(
                source,
                timeout=timeout,                      # Maksymalny czas oczekiwania na rozpoczęcie mowy
                phrase_time_limit=phrase_time_limit   # Maksymalna długość nagrywanej wypowiedzi
            )
            print("⏳ Rozpoznaję...")

            # Rozpoznaj tekst z nagrania przy użyciu API Google (dla języka polskiego)
            text = recognizer.recognize_google(audio, language="pl-PL")
            return f"Powiedziałeś {text}"   # Zwróć rozpoznaną wypowiedź jako tekst
        
        except sr.WaitTimeoutError:
            # Użytkownik nie rozpoczął mówienia w określonym czasie
            return "Nie wykryto głosu – limit czasu."
        
        except sr.UnknownValueError:
            # Dźwięk został zarejestrowany, ale nie udało się rozpoznać słów
            return "Nie zrozumiałem – powtórz proszę."
        
        except sr.RequestError:
            # Wystąpił problem z połączeniem do serwisu rozpoznawania mowy
            return "Błąd połączenia z serwisem rozpoznawania mowy."
