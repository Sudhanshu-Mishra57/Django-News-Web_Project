from datetime import date

def today():
    today = date.today()
    data = today.strftime('%d-%m-%Y')
    return data[0:]