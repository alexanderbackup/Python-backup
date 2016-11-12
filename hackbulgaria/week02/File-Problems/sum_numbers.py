# sum_numbers.py
import sys


def main():
    sys.argv[0] = 'sum_numbers.py'
    filename = sys.argv[1]
    with open(filename) as f:
        print(sum([int(i) for i in f.read().strip().split(' ')]))
        


if __name__ == '__main__':
    main()
