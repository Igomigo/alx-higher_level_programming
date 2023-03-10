#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    arg = sys.argv
    length = len(sys.argv) - 1

    if length == 1:
        print("{} argument:".format(length))
        print("{}: {}".format(length, arg[1]))

    elif length == 0:
        print("{} arguments.".format(length))

    elif length > 1:
        print("{} arguments:".format(length))
        for i in range(1, length + 1):
            print("{}: {}".format(i, arg[i]))
