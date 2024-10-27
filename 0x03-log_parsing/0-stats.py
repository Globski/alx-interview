#!/usr/bin/python3
import sys
import signal

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def process_line(line):
    global total_size, line_count
    try:
        parts = line.split()
        if len(parts) < 2:
            return  # Skip lines that don’t match the format
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1
        line_count += 1
    except Exception:
        pass  # Handle lines with unexpected formats gracefully

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        process_line(line.strip())
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
