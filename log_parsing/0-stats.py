#!/usr/bin/python3
"""Read log lines from stdin and display cumulative statistics."""

import sys


STATUS_CODES = (200, 301, 400, 401, 403, 404, 405, 500)


def print_stats(total_size, status_counts):
    """Print total file size and known HTTP status frequencies."""
    print("File size: {}".format(total_size))
    for code in STATUS_CODES:
        if status_counts[code]:
            print("{}: {}".format(code, status_counts[code]))
    sys.stdout.flush()


def main():
    """Read and count log lines, printing every ten lines and at EOF."""
    total_size = 0
    counts = {code: 0 for code in STATUS_CODES}
    lines = 0

    try:
        for line in sys.stdin:
            lines += 1
            fields = line.split()
            if len(fields) >= 2:
                try:
                    total_size += int(fields[-1])
                except ValueError:
                    pass
                try:
                    status = int(fields[-2])
                except ValueError:
                    status = None
                if status in counts:
                    counts[status] += 1

            if lines % 10 == 0:
                print_stats(total_size, counts)
    except KeyboardInterrupt:
        print_stats(total_size, counts)
        return

    if lines % 10 != 0 or lines == 0:
        print_stats(total_size, counts)


if __name__ == "__main__":
    main()
