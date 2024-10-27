#!/usr/bin/python3
"""
This script reads log entries from standard input and computes statistics
about HTTP response codes and total file sizes. It processes each line of
input, summing file sizes and counting occurrences of specified status codes.

The expected input format for each log entry is:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Statistics are printed after every 10 lines processed and also on keyboard
interruption (CTRL + C).

Usage:
    ./0-generator.py | ./0-stats.py
"""

import sys
from collections import defaultdict


def parse_log():
    """
    Reads log entries from standard input and calculates statistics.

    This function maintains a running total of the file sizes and counts
    occurrences of specific HTTP status codes (200, 301, 400, 401, 403, 404, 405, 500).
    It processes each line of input and updates the metrics accordingly.

    The function prints the statistics after every 10 valid log entries
    and handles keyboard interruption gracefully by printing the final statistics.
    """
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) < 7:
                continue
            
            try:
                ip = parts[0]
                date = parts[2][1:] + ' ' + parts[3][:-1]
                method = parts[4]
                status_code = int(parts[5])
                file_size = int(parts[6])

                if status_code in {200, 301, 400, 401, 403, 404, 405, 500}:
                    status_codes[status_code] += 1
                    total_size += file_size
            
            except (ValueError, IndexError):
                continue

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
            
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)

def print_stats(total_size, status_codes):
    """
    Prints the current statistics of the log parsing.

    Args:
        total_size (int): The accumulated total file size from the parsed logs.
        status_codes (dict): A dictionary with counts of each status code.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

if __name__ == "__main__":
    parse_log()
