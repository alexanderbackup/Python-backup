# cat.py
import sys


def main():
    sys.argv[0] = 'cat.py'
    try:
        file_path = sys.argv[1]
    
        with open(file_path) as f:
            print(f.read().strip())
    except:
        print("Need 1 more Argument!")


if __name__ == '__main__':
    main()
