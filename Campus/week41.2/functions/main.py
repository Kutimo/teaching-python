# log message

def log_message(message: str, level: str = "info") -> str:
    return f"[{level}] {message} "


print(log_message("System started"))
print(log_message("Disk is almost full", "WARN"))
