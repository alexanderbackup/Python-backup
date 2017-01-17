#import os
from Mouse_Coords import mouse_coords
from time import sleep

# Not finished

def main():
    while True:
        yield mouse_coords()

def beep():
    print('\a')
           
if __name__ == '__main__':
    gen = main()
    for i in gen:
        print(i)
        sleep(0.5)
