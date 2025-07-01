import locale
from datetime import datetime

def set_polish_locale():
    try:
        locale.setlocale(locale.LC_TIME, 'pl_PL.UTF-8')
    except locale.Error:
        locale.setlocale(locale.LC_TIME, 'polish')

def get_formatted_date_time():
    now = datetime.now()
    formatted_date = now.strftime("%A, %d %B")
    current_time = now.strftime("%H:%M")
    return current_time, formatted_date