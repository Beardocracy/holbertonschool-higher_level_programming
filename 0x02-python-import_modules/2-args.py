#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)

    print('{} argument{}'.format(args - 1, 's' if args != 2 else ''), end='')
    print('{}'.format('.' if args == 1 else ':'))
    i = 1
    for arg in sys.argv[1:]:
        print('{}: {}'.format(i, arg))
        i += 1
