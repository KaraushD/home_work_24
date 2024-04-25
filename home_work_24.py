from datetime import datetime

def get_days_from_today(date):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.now()
        delta = current_date - date_obj
        return delta.days
    except ValueError:
        print("Помілка: неправильний формат дати. Введіть дату у форматі 'YYYY-MM-DD'.")
date = '2024-04-07'
result = get_days_from_today(date)
if result is not None:
    print("Кількість днів від заданої дати до поточної:", result)