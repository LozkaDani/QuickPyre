import datetime

def time_cmd():
    current_date_time = datetime.datetime.now()
    current_time = datetime.datetime.now().time()
    print(current_time)