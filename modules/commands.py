from modules import speech_input, speech_output

def listen_loop(engine):
    while True:
        command = speech_input.recognize_speech_from_mic()

        if is_exit_command(command):
            speech_output.speak_message(engine, "W porządku. Pamiętaj, że zawsze jestem dla Ciebie. Do usłyszenia.")
            break

        speech_output.speak_message(engine, command, voice_index=0)


def is_exit_command(command):
    return any(phrase in command.lower() for phrase in ["kończymy", "koniec", "zamknij", "do widzenia"])