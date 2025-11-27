import re

# Regex patterns
ip_pattern = re.compile(r'\d{1,3}(\.\d{1,3}){3}')
status_pattern = re.compile(r'"\s*(\d{3})\s')

# Dictionaries
ip_count = {}
status_count = {}
ip_status = {}

with open("app.log", "r") as file:
    for line in file:
        # Extract matches
        ip_match = ip_pattern.search(line)
        status_match = status_pattern.search(line)

        # Extract values
        if ip_match:
            ip = ip_match.group()
        else:
            ip = None

        if status_match:
            status = status_match.group(1)
        else:
            status = None

        # Count IPs
        if ip:
            ip_count[ip] = ip_count.get(ip, 0) + 1

        # Count Statuses
        if status:
            status_count[status] = status_count.get(status, 0) + 1

        # Nested dictionary (IP → Status → count)
        if ip and status:
            if ip not in ip_status:
                ip_status[ip] = {}
            ip_status[ip][status] = ip_status[ip].get(status, 0) + 1

# Print results
print("IP COUNT:")
for ip, count in ip_count.items():
    print(ip, count)

print("\nSTATUS COUNT:")
for status, count in status_count.items():
    print(status, count)

print("\nIP → STATUS MAP:")
for ip, status_dict in ip_status.items():
    print(ip, status_dict)
