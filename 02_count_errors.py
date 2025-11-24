# Counts how many ERROR lines are present

count = 0

with open("sample_logs/app.log", "r") as f:
    for line in f:
        if "ERROR" in line:
            count += 1

print("Total ERROR lines:", count)
