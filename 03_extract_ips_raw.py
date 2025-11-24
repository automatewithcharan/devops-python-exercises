# Extract all words containing "." (not validated)

with open("sample_logs/app.log", "r") as f:
    for line in f:
        parts = line.split()
        for word in parts:
            if "." in word:
                print(word)
