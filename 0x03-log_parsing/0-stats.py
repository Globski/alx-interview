#!/usr/bin/python3
import sys

# Initialize metrics
total_file_size = 0
status_counts = {
    "200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0
}
line_count = 0

def print_stats():
    """Print the accumulated metrics"""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

try:
    for line in sys.stdin:
        parts = line.strip().split()
        
        # Ensure line format
        if len(parts) < 7:
            continue
        
        # Extract file size and status code
        file_size = parts[-1]
        status_code = parts[-2]
        
        # Update file size
        try:
            total_file_size += int(file_size)
        except ValueError:
            continue
        
        # Update status code count
        if status_code in status_counts:
            status_counts[status_code] += 1
        
        # Increment line count and print stats every 10 lines
        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # On keyboard interrupt, print the final stats
    print_stats()
    raise

# Final print in case the input ends without interruption
print_stats()
