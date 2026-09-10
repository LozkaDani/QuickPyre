from pathlib import Path
from datetime import datetime, date, time
def ls_cmd(flags):
    if flags == []:
        current_dir = Path(".")
        items = list(current_dir.iterdir()) #list of items in dir
        for item in items:
            print(f"{item} DIR") if item.is_dir() else print(f"{item} {item.suffix.upper()}")
    if "-t" in flags:
        current_dir = Path(".")
        items = list(current_dir.iterdir())
        for item in items:
            item_path = Path(item)
            timestamp = item_path.stat().st_ctime
            date, understandable_time = str(datetime.fromtimestamp(timestamp)).split(" ", 1)
            
            hours, minutes_seconds = understandable_time.split(":", 1)
            minutes, seconds = minutes_seconds.split(":", 1)
            hours_minutes = f"{hours}:{minutes}"
            
            understandable_date = str(datetime.fromtimestamp(timestamp).date()).replace("-", ".")
            yy, mm = understandable_date.split(".", 1)
            mm, dd = mm.split(".", 1)
            mm_name = check_month(mm)
            print(f"{mm_name} {mm} {hours_minutes} {item} DIR") if item.is_dir() else print(f"{mm_name} {mm} {hours_minutes} {item} {item.suffix.upper()}")

def check_month(mm):
    months = {
        "01": "Jan",
        "02": "Feb",
        "03": "Mar",
        "04": "Apr",
        "05": "May",
        "06": "Jun",
        "07": "Jul",
        "08": "Aug",
        "09": "Sep",
        "10": "Oct",
        "11": "Nov",
        "12": "Dec",
    }
    mm_name = months.get(mm, mm)
    return mm_name