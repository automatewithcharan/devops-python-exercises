# Extract UNIQUE valid IPs (no duplicates)

seen = set()

with open("sample_logs/app.log", "r") as f:
    for line in f:
        parts = line.split()
        for word in parts:
            if "." in word:
                pieces = word.split(".")
                if len(pieces) == 4:
                    if all(p.isdigit() for p in pieces):
                        if all(0 <= int(p) <= 255 for p in pieces):
                            seen.add(word)

print("Unique IPs:", seen)
print("Total unique:", len(seen))
