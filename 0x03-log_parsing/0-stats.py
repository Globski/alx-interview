#!/usr/bin/python3
"""
A script for parsing HTTP request logs.
Reads from stdin and computes statistics about response codes and file sizes.
"""
import sys
import re
from collections import defaultdict
import signal

# Initialize statistics
total_file_size = 0
status_codes = defaultdict(int)
line_count = 0

def signal_handler(sig, frame):
    """Handles keyboard interruption (CTRL + C) gracefully."""
    print("\nExiting gracefully...")
    print_statistics()
    sys.exit(0)

def print_statistics():
    """Prints the current statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def parse_log_line(line):
    """Parses a single line of the log."""
    global total_file_size, line_count
    pattern = r'(?P<ip>[\d\.]+) - \[(?P<date>.+?)\] "GET /projects/260 HTTP/1\.1" (?P<status_code>\d{3}) (?P<file_size>\d+)'
    match = re.match(pattern, line)
    if match:
        status_code = match.group('status_code')
        file_size = int(match.group('file_size'))

        # Update metrics
        total_file_size += file_size
        status_codes[status_code] += 1
        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

if __name__ == "__main__":
    # Setup signal handling
    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            parse_log_line(line)
    except EOFError:
        print_statistics()
