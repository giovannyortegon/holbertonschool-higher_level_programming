#!/usr/bin/python3
def main():
    from sys import argv
    argc = 0
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(argc))
        for arg in range(1, argc + 1):
            print("{}: {}".format(arg, argv[arg]))


if __name__ == '__main__':
    main()
