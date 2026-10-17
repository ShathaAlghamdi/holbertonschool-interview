
#!/usr/bin/python3
"""Parse HTTP logs and print statistics."""

import sys


def print_stats(total_size, status_counts):
    """Print the accumulated statistics."""
    print("File size: {}".format(total_size))

    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

    sys.stdout.flush()


def main():
    """Read log lines and compute statistics."""
    total_size = 0
    line_count = 0
    status_counts = {}
    valid_codes = ("200", "301", "400", "401",
                   "403", "404", "405", "500")

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) >= 2:
                try:
                    total_size += int(parts[-1])
                except ValueError:
                    pass

                status = parts[-2]
                if status in valid_codes:
                    status_counts[status] = (
                        status_counts.get(status, 0) + 1
                    )

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        return

    if line_count == 0 or line_count % 10 != 0:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
