#!/usr/bin/python3
import re
import sys
from collections import defaultdict

def extract_input(line):
    pattern = r'(?P<ip>\S+) - \[(?P<date>.*?)\] "(?P<request>.*?)" (?P<status_code>\d{3}) (?P<file_size>\d+)'
    match = re.match(pattern, line)
    if match:
        return {
            'status_code': match.group('status_code'),
            'file_size': int(match.group('file_size')),
        }
    return None

def print_statistics(total_size, status_codes):
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def run():
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_info = extract_input(line)
            if line_info:
                total_size += line_info['file_size']
                status_codes[line_info['status_code']] += 1
                line_count += 1
                if line_count % 10 == 0:
                    print_statistics(total_size, status_codes)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_size, status_codes)

if __name__ == "__main__":
    run()
