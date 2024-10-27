#!/usr/bin/python3
'''A script for parsing HTTP request logs using an alternative logic.
'''
import re
from collections import defaultdict

def parse_log_entry(line):
    '''Parses a single HTTP log entry line.
    '''
    log_pattern = (
        r'(?P<ip>\S+)\s+-\s+\[(?P<date>[^\]]+)\]\s+"(?P<request>[^"]+)"\s+'
        r'(?P<status_code>\d{3})\s+(?P<file_size>\d+)'
    )
    match = re.fullmatch(log_pattern, line)
    if match:
        return match.group('status_code'), int(match.group('file_size'))
    return None, 0

def print_log_stats(total_file_size, status_counts):
    '''Prints cumulative file size and status code counts.
    '''
    print('File size:', total_file_size)
    for status_code, count in sorted(status_counts.items()):
        print(f'{status_code}: {count}')

def process_logs():
    '''Main function for processing HTTP request logs.
    '''
    total_file_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        while True:
            line = input()
            status_code, file_size = parse_log_entry(line)
            if status_code:
                status_counts[status_code] += 1
            total_file_size += file_size
            line_count += 1

            if line_count % 10 == 0:
                print_log_stats(total_file_size, status_counts)
    except (KeyboardInterrupt, EOFError):
        print_log_stats(total_file_size, status_counts)

if __name__ == '__main__':
    process_logs()
