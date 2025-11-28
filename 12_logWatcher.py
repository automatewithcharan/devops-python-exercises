import time
import re

ip_pattern = re.compile(r'\d{1,3}(\.\d{1,3}){3}')
status_pattern = re.compile(r'"\s*(\d{3})\s')

with open("app.log", "r") as f:
    f.seek(0, 2)   # Move to end of file

    while True:
        line = f.readline()

        if not line:
            time.sleep(0.1)
            continue

        ip_match = ip_pattern.search(line)
        status_match = status_pattern.search(line)

        if ip_match:
            ip = ip_match.group()
        else:
            ip = None

        if status_match:
            status = status_match.group(1)
        else:
            status = None

        if status and int(status) >= 400:
            print(f"ALERT: {ip} returned {status}")
