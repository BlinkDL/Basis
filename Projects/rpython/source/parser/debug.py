DEBUG = {
    "STATEMENT": False,
    "IMPORT": True,
}


def debug_print(head, string=None):
    if string is None:
        print(f"{head}")
    else:
        print("\033[36m" + head + ":\033[0m")
        print(f"{string}")
