from os import remove
from sys import exit
from random import sample
import loremipsum as LM
from pathlib import Path


CHAPTERS_COUNT = 4 # Chapters count
CHAPTERS_RANGE = range(200, 300) # Chapter length range (in words)

def main(chapters_count, chapter_length_range: 'in words'):

    word_range = set(i for i in chapter_length_range)
    word_range.add(max(word_range)+1)
    
    for _new_chapter in range(chapters_count):
        num_words_in_chapter = sample(word_range, 1)[0]
        chapter = ''
        while num_words_in_chapter > 0:
            new_sent = LM.generate_sentence()
            chapter += new_sent[2] # should be str
            num_words_in_chapter -= new_sent[1] # should be int
        yield chapter
    
 
if __name__ == '__main__':
    my_file = Path('new_book.txt')
    if my_file.is_file():
        while True:
            ans = input('Do you want to replace "new_book.txt"? Y/n: ')
            ans = ans.lower()
            if ans == 'n' or ans == 'no':
                exit()
            elif ans == 'y' or ans == 'yes':
                remove('new_book.txt')
                break
            else:
                print('Wront Imput!')
    gen = main(CHAPTERS_COUNT, CHAPTERS_RANGE)
    with open('new_book.txt', 'w') as f:
        counter = 1
        for _chapter in gen:
            f.write('\n#Chapter {}\n'.format(counter))
            f.write(_chapter)
            counter += 1
    
    
    
