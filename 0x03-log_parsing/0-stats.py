#!/usr/bin/python3

import sys  # Import the sys module to work with standard input
import re   # Import the re module to use regular expressions
import signal  # Import signal to handle keyboard interruptions

# Initialize statistics
total_size = 0  # Variable to hold the cumulative file size
status_counts = {  # Dictionary to count occurrences of each status code
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0  # Counter for the number of lines processed

def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C) to exit gracefully."""
    print("\nExiting gracefully...")  # Inform the user that the script is exiting
    print_summary()  # Print the current statistics
    sys.exit(0)  # Exit the program

def print_summary():
    """Print the total file size and counts of status codes."""
    print(f"File size: {total_size}")  # Output the total file size
    for status in sorted(status_counts.keys()):  # Iterate through status codes in ascending order
        if status_counts[status] > 0:  # Only print status codes that have occurrences
            print(f"{status}: {status_counts[status]}")  # Output the count for each status code

def parse_log_line(line):
    """Parse a single line of log data."""
    global total_size, line_count  # Declare total_size and line_count as global to modify them

    # Regex pattern to match log entries
    pattern = r'(?P<ip>[\d\.]+) - \[\S+\] "GET /projects/260 HTTP/1\.1" (?P<status>\d{3}) (?P<size>\d+)'
    match = re.match(pattern, line)  # Try to match the line with the regex pattern
    if match:  # If there's a match, proceed
        status = int(match.group('status'))  # Extract and convert the status code to an integer
        size = int(match.group('size'))  # Extract and convert the file size to an integer

        # Update total size and counts
        total_size += size  # Add the current file size to the total
        if status in status_counts:  # Check if the status code is one we are tracking
            status_counts[status] += 1  # Increment the count for the corresponding status code

        line_count += 1  # Increment the line count

        # Print summary every 10 lines
        if line_count % 10 == 0:  # If 10 lines have been processed
            print_summary()  # Print the current statistics

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)  # Register the signal handler for CTRL + C

    try:
        for line in sys.stdin:  # Read lines from standard input one by one
            parse_log_line(line)  # Parse each line
    except Exception as e:  # Catch any exceptions that occur
        print(f"Error processing input: {e}")  # Print the error message
        print_summary()  # Print the statistics before exiting
