# cat2.py
import sys


def main():
    for i in range(1, len(sys.argv)):
        with open(sys.argv[i]) as f:
            print(f.read())

if __name__ == '__main__':
    main()
