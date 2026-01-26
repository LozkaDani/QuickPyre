import calendar
def calendar_cmd():
    yy = int(input("Enter year: "))
    mm = int(input("Enter month(1, 2, 3..): "))
    print(calendar.month(yy, mm))