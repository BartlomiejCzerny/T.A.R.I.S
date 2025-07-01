from modules import utils
from modules import speech_output

def main():
    utils.set_polish_locale()
    current_time, formatted_date = utils.get_formatted_date_time()

    message = (
        f"Hej. Jestem TARIS, Twój asystent. Jest godzina {current_time}, {formatted_date}. Niech Twoja pasja prowadzi Cię do wielkich rzeczy!"
    )

    engine = speech_output.init_engine()
    speech_output.speak_message(engine, message, voice_index=0)

if __name__ == "__main__":
    main()