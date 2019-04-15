#!/usr/bin/python

## Add formal header
import os
import sys
import random
import dictionary

def main():
    if len(sys.argv) != 2:
        usage()
        quit()

    print('Welcome to Korean Flashcards')
    print('')
    keyin = ''
    while keyin != 'q':
        card = get_rand_card()
        #print(card['korean'])
        #print('')
        keyin = raw_input('p to play audio, n to show answer, q to quit: ')

def get_rand_card():
    try:
        return dictionary[sys.argv[1]-1]
    except:
        usage()
        quit()
        
def usage():
    print('Usage: flashcardsKtoE.py [Chapter No.]')
    print('e.g.   flashcardsKtoE.py 7')
        
#{'english' : 'blah', 'korean' : ('blah', 'path sound')}
if __name__ == "__main__":
    main()
