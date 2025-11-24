# Demonstration of splitting and joining

line = "ERROR Disk full on 10.0.0.1"
parts = line.split()
timestamp = " ".join(parts[:2])
message = " ".join(parts[2:])

print("Parts:", parts)
print("Timestamp:", timestamp)
print("Message:", message)
