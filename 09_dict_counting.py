# Practice dictionary counting logic

items = ["A", "A", "B", "C", "A"]

counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1

print(counts)
