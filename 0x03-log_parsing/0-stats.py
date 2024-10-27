#!/usr/bin/python3
"""
A script that reads lines of HTTP logs from standard input, parses specific information,
and prints summary statistics every 10 lines or upon keyboard interruption (CTRL + C).
"""

import sys
import signal

# Global variables to track metrics
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Prints the total file size and count of each status code."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def process_line(line):
    """
    Parses a single log line and updates global metrics if the line matches the required format.
    
    Expected format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    """
    global total_size, line_count
    try:
        parts = line.split()
        if len(parts) < 2:
            return  # Skip lines that don’t match the expected format
        
        # Extract the status code and file size from the line
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        
        # Update total file size and status code count
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1
        line_count += 1
    except Exception:
        pass  # Skip lines with unexpected formats

def signal_handler(sig, frame):
    """Handles keyboard interruptions and prints current statistics before exiting."""
    print_stats()
    sys.exit(0)

# Register signal handler for keyboard interruption (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        process_line(line.strip())
        # Print stats every 10 lines
        if line_count % 10 == 0 and line_count > 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
