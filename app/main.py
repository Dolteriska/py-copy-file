
def copy_file(command: str) -> None:
    command_ls = command.split(" ")
    if command_ls[0] != "cp":
        return None
    try:
        if command_ls[1] == command_ls[2]:
            return None
        with (open(command_ls[1], "r") as file_in,
              open(command_ls[2], "w") as file_out):
            content = file_in.read()
            file_out.write(content)
    except Exception:
        return None
