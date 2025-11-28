import re
import argparse

# ---- CLI ARGUMENTS ----
parser = argparse.ArgumentParser()
parser.add_argument("--file", required=True, help="path of the log file")
parser.add_argument("--top", type=int, default=5, help="how many top offenders are required")
args = parser.parse_args()

# ---- REGEX PATTERNS ----
ip_pattern = re.compile(r'\d{1,3}(\.\d{1,3}){3}')
status_pattern = re.compile(r'"\s*(\d{3})\s')

# ---- STORE STATUS PER IP ----
ip_status = {}

with open(args.file, "r") as f:
    for line in f:
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

        if ip and status:
            if ip not in ip_status:
                ip_status[ip] = {}
            ip_status[ip][status] = ip_status[ip].get(status, 0) + 1

# ---- ERROR COUNTS PER IP ----
ip_errors = {}

for ip, statuses in ip_status.items():
    total_errors = 0
    for status, count in statuses.items():
        if int(status) >= 400:
            total_errors += count
    ip_errors[ip] = total_errors

# ---- SORT AND PRINT TOP N ----
top_offenders = sorted(ip_errors.items(), key=lambda item: item[1], reverse=True)
top_n = top_offenders[:args.top]

for ip, errors in top_n:
    print(ip, errors)
