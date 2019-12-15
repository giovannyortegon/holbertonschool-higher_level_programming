#!/usr/bin/python3
def main():
    from sys import argv
    argc = 0
    add = 0
    argc = len(argv) - 1
    if argc == 0:
        print("{}".format(argc))
    elif argc == 1:
        print("{}".format(argv[argc]))
    else:
        for num in range(1, argc + 1):
            add = add + int(argv[num])
        print("{}".format(add))


if __name__ == '__main__':
    main()
