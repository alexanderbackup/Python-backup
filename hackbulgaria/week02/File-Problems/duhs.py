# duhs.py
import sys, os


def main():
    sys.argv[0] = 'duhs.py'
    folder = sys.argv[1]
    folder_size = 0
    try:
        for (path, dirs, files) in os.walk(folder):
            for file in files:
                filename = os.path.join(path, file)
                folder_size += os.path.getsize(filename)

        print ("%0.1f MB" % (folder_size/(1024*1024.0)))
    except:
        print("File path does not exist")

if __name__ == '__main__':
    main()

# determine size of a given folder in MBytes


# pick a folder you have ...

