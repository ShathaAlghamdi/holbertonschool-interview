#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
Prints total file size and number of lines by status code 
every 10 lines and/or upon keyboard interruption (CTRL + C).
"""
import sys

total_file_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


def print_stats():
    """Prints the accumulated metrics: total file size and status codes."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 7:
            try:
                file_size = int(parts[-1])
                status_code = parts[-2]

                total_file_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1

                line_count += 1
            except ValueError:
                pass

        if line_count == 10:
            print_stats()
            line_count = 0

except KeyboardInterrupt:
    print_stats()
    raise

finally:
    if line_count > 0:
        print_stats()
