def history_cmd(path_to_history, colors):
    try:
        with open(path_to_history, "r") as f:
            history = f.readlines()
        #print(date, time, cmd)
        for item in history:
            date_time, cmd = item.split("|", 1)
            date, time = date_time.split(" ", 1)
            time = time.strip()
            print(f"{colors.Colors.CYAN}{date} {time}{colors.Colors.END} | {cmd}{colors.Colors.END}") #{colors.Colors.BLUE}
    except Exception as e:
        print(f"history: {e}")