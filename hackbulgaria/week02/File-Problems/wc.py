# wc.py
import sys

def main():
    sys.argv[0] = 'wc.py'
    try:
        filename = sys.argv[2]
        
        with open(filename) as f:
            story = f.read()
        if sys.argv[1] == 'chars':
            print(len(story))
        elif sys.argv[1] == 'words':
            print(len(story.split()))
        elif sys.argv[1] == 'lines':
            print(len(story.strip().split('\n')))
        else:
            raise ValueError()
    except:
        print('Invalid arguments or text file does not exist!')


if __name__ == '__main__':
    main()
