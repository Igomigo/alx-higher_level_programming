#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics
"""


def stats(a_size, status_code):
    """Print computed metrics.
    Args:
        a_size (int): accumulated read file size.
        status_code (dict): accumulated count of status codes.
    """
    print("File size: {}".format(a_size))
    for key in sorted(status_code):
        print("{}: {}".format(key, status_code[key]))


if __name__ == "__main__":
    import sys

    a_size = 0
    status_code = {}
    valid_code = ['200', '301', '400', '401', '403', '404', '405', '500']
    c = 0

    try:
        for line in sys.stdin:
            if c == 10:
                stats(a_size, status_code)
                c = 1
            else:
                c += 1
            line = line.split()
            try:
                a_size += int(line[-1])
            except (IndexError, ValueError):
                pass
            try:
                if line[-2] in valid_code:
                    if status_code.get(line[-2], -1) == -1:
                        status_code[line[-2]] = 1
                    else:
                        status_code[line[-2]] += 1
            except IndexError:
                pass

        stats(a_size, status_code)

    except KeyboardInterrupt:
        stats(a_size, status_code)
        raise
