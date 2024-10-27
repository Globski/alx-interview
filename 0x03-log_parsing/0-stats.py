#!/usr/bin/python3

import sys
import re
import signal

total_size = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

def signal_handler(sig, frame):
    print("\nExiting gracefully...")
    print_summary()
    sys.exit(0)

def print_summary():
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

def parse_log_line(line):
    global total_size, line_count

    pattern = r'(?P<ip>[\d\.]+) - \[\S+\] "GET /projects/260 HTTP/1\.1" (?P<status>\d{3}) (?P<size>\d+)'
    match = re.match(pattern, line)
    if match:
        status = int(match.group('status'))
        size = int(match.group('size'))

        # Update total size and counts
        total_size += size
        if status in status_counts:
            status_counts[status] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_summary()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            parse_log_line(line)
    except Exception as e:
        print(f"Error processing input: {e}")
        print_summary()
