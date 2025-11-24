# Find most frequent IP address

counts = {}

with open("sample_logs/app.log", "r") as f:
    for line in f:
        parts = line.split()
        for word in parts:
            if "." in word:
                pieces = word.split(".")
                if len(pieces) == 4:
                    if all(p.isdigit() for p in pieces):
                        if all(0 <= int(p) <= 255 for p in pieces):
                            counts[word] = counts.get(word, 0) + 1

top_ip = max(counts, key=counts.get)

print("Most active IP:", top_ip, "Hits:", counts[top_ip])
