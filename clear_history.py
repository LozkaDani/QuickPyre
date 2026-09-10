def clear_history_cmd(path_to_history):
    try:
        with open(path_to_history, "w") as f:
            f.write("DATE TIME | CMD\n")
    except Exception as e:
        print(f"clear_history: {e}")