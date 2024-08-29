
#!/usr/bin/python3
import sys
import re
from collections import defaultdict
import signal
import functools

# Initialize variables
total_file_size = 0
status_codes_count = defaultdict(int)
line_count = 0
lines_per_print = 10

# Regular expression to match the log line format
log_pattern = re.compile(
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[.*?\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)

def handle_interrupt(signum, frame):
    print_metrics()
    sys.exit(0)

def print_metrics():
    # Print total file size
    print(f"File size: {total_file_size}")
    
    # Print status codes count
    for status_code in sorted(status_codes_count.keys()):
        print(f"{status_code}: {status_codes_count[status_code]}")

def process_line(line):
    global total_file_size
    global status_codes_count
    global line_count

    match = log_pattern.match(line)
    if match:
        ip, status_code, file_size = match.groups()
        file_size = int(file_size)
        status_code = int(status_code)
        
        # Update metrics
        total_file_size += file_size
        status_codes_count[status_code] += 1
        line_count += 1

        # Print metrics if the line count is a multiple of lines_per_print
        if line_count % lines_per_print == 0:
            print_metrics()

# Set up signal handler for keyboard interruption
signal.signal(signal.SIGINT, handle_interrupt)

# Read from stdin line by line
for line in sys.stdin:
    process_line(line)

# Final metrics print after reading all lines
print_metrics()