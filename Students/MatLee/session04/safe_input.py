def safe_input(display=""):
    try:
        return raw_input(display)
    except (EOFError, KeyboardInterrupt):
        return None
