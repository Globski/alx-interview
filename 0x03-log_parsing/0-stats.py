#!/usr/bin/python3
"""
A script for parsing HTTP request logs.
Reads from stdin and computes statistics about response codes and file sizes.
"""
import sys
import re
from collections import defaultdict

def extract_log_data(log_line):
    """Extracts relevant data from a single log line."""
    pattern = r'(?P<ip>\S+) - \[(?P<date>.*?)\] "(?P<request>.*?)" (?P<status_code>\d{3}) (?P<file_size>\d+)'
    match = re.match(pattern, log_line)
    if match:
        return {
            'status_code': match.group('status_code'),
            'file_size': int(match.group('file_size')),
        }
    return None

def print_statistics(total_file_size, status_code_counts):
    """Prints the accumulated statistics of the HTTP request log."""
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_code_counts):
        if status_code_counts[status_code] > 0:
            print(f"{status_code}: {status_code_counts[status_code]}")

def main():
    total_file_size = 0
    status_code_counts = defaultdict(int)
    line_count = 0

    try:
        for log_line in sys.stdin:
            log_data = extract_log_data(log_line)
            if log_data:
                total_file_size += log_data['file_size']
                status_code_counts[log_data['status_code']] += 1
                line_count += 1

                # Print statistics every 10 lines
                if line_count % 10 == 0:
                    print_statistics(total_file_size, status_code_counts)
                    
    except (KeyboardInterrupt, EOFError):
        # Final output on interruption
        print_statistics(total_file_size, status_code_counts)

if __name__ == "__main__":
    main()
