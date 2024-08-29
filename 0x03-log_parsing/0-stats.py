#!/usr/bin/python3
import sys

# Initialize variables to store total file size and status code counts
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Prints the current statistics of file size and status codes."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

try:
    # Read from standard input line by line
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        
        # Check if line has the correct number of elements
        if len(parts) < 7:
            continue
        
        try:
            # Extract status code and file size
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update total file size
            total_file_size += file_size
            
            # Update status code count if it is one of the expected codes
            if status_code in status_codes:
                status_codes[status_code] += 1

        except (ValueError, IndexError):
            # Skip lines that don't have the correct format
            continue

        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print stats on keyboard interruption (CTRL + C)
    print_stats()
    raise
