def display_current_datetime():
    import datetime
    current_date = datetime.datetime.now()
    print(current_date)
def calculate_future_date():
    import datetime
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=10)
    print(future_date)
