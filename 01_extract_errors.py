# Prints all ERROR lines from the log file

with open("sample_logs/app.log", "r") as f:
    for line in f:
        if "ERROR" in line:
            print(line.strip())
