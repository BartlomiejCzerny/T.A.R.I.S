import locale                   # Import modułu do obsługi lokalizacji (język, formaty daty i czasu)
from datetime import datetime   # Import klasy datetime do pracy z datą i czasem

def set_polish_locale():
    # Próbuj ustawić polską lokalizację w formacie UTF-8 (Linux, macOS)
    try:
        locale.setlocale(locale.LC_TIME, 'pl_PL.UTF-8')
    except locale.Error:
        # Jeśli nie uda się, spróbuj ustawić polską lokalizację w innej nazwie (np. Windows)
        locale.setlocale(locale.LC_TIME, 'polish')

def get_formatted_date_time():
    # Pobierz aktualny czas i datę
    now = datetime.now()

    # Sformatuj datę jako: pełna nazwa dnia tygodnia, dzień i nazwa miesiąca
    formatted_date = now.strftime("%A, %d %B")

    # Sformatuj czas jako godzina i minuty
    current_time = now.strftime("%H:%M")

    # Zwróć czas i datę jako krotkę
    return current_time, formatted_date