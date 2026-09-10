import shlex
def echo_cmd(args, cmd):
    if not cmd:
        print("echo: missing operand.")
        return
    
    parts = shlex.split(cmd, posix=False)

    if ">" in parts:
        arrow_index = parts.index(">")
        
        if arrow_index + 1 < len(parts):
            text_parts = parts[:arrow_index]
            path = " ".join(parts[arrow_index+1:])

            text = " ".join(text_parts)

            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
        else:
            print("echo: missing operand")
    else:
        print(" ".join(args))
