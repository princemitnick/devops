def log():
    logs = [
        "INFO Server started",
        "ERROR Disk space low",
        "WARNING High memory usage",
        "INFO Connection established",
        "ERROR Database connection lost"
    ]
    with open("system.log", "w") as f:
        for line in logs:
            f.write(f"{line}\n")

    with open("system.log", "r") as f:
        for line in f:
            if "ERROR" in line:
                print(line.strip())

if __name__ == "__main__":
    log()