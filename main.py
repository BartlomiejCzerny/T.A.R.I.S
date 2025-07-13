from modules import utils           # Import modułu z funkcjami narzędziowymi (np. data, czas, lokalizacja)
from modules import speech_output   # Import modułu odpowiedzialnego za syntezę mowy (text-to-speech)
from modules import speech_input    # Import modułu do rozpoznawania mowy (speech-to-text)

def main():
    # Ustaw lokalizację na polską, aby format daty i czasu odpowiadał polskim standardom
    utils.set_polish_locale()

    # Pobierz aktualny czas oraz sformatowaną datę jako łańcuch znaków
    current_time, formatted_date = utils.get_formatted_date_time()

    # Przygotuj powitalną wiadomość z aktualnym czasem i datą
    message = (
        f"Hej. Jestem TARIS, Twój asystent. Jest godzina {current_time}, {formatted_date}. Niech Twoja pasja prowadzi Cię do wielkich rzeczy!"
    )

    # Inicjalizuj silnik syntezy mowy (text-to-speech)
    engine = speech_output.init_engine()

    # Odtwórz przygotowaną wiadomość głosowo, korzystając z wybranego głosu (voice_index=0)
    speech_output.speak_message(engine, message, voice_index=0)

    # Odbierz komendę głosową z mikrofonu i zapisz ją jako tekst
    command = speech_input.recognize_speech_from_mic()
    
    # Powtórz na głos usłyszaną komendę, poprzedzając ją zwrotem "Powiedziałeś"
    speech_output.speak_message(engine, f"Powiedziałeś {command}", voice_index=0)

if __name__ == "__main__":
    # Punkt startowy aplikacji — wywołanie funkcji main przy uruchomieniu skryptu
    main()