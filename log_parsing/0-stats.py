#!/usr/bin/python3
"""Parse HTTP access logs from standard input."""
import re
import sys


PATTERN = re.compile(
    r'^\S+ - \[[^\]\r\n]+\] "GET /projects/260 HTTP/1\.1" (\S+) (\d+)$'
)
CODES = (200, 301, 400, 401, 403, 404, 405, 500)


def display(total, counts):
    """Print cumulative metrics in ascending status-code order."""
    print("File size: {}".format(total), flush=True)
    for code in CODES:
        if counts[code]:
            print("{}: {}".format(code, counts[code]), flush=True)


def main():
    """Consume lines and report results every ten lines or on interrupt."""
    total = 0
    counts = {code: 0 for code in CODES}
    lines = 0
    try:
        for line in sys.stdin:
            lines += 1
            match = PATTERN.fullmatch(line.rstrip('\r\n'))
            if match:
                code_text, size_text = match.groups()
                total += int(size_text)
                try:
                    code = int(code_text)
                except ValueError:
                    code = None
                if code in counts:
                    counts[code] += 1
            if lines % 10 == 0:
                display(total, counts)
    except KeyboardInterrupt:
        display(total, counts)
    else:
        if lines % 10 != 0:
            display(total, counts)


if __name__ == "__main__":
    main()
