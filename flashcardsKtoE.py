#!/usr/bin/python
# -*- coding: utf-8 -*-

######################################################
# Title: Korean_Flashcards.py
# Author: Jason C Zimmerman
# Date: 4/16/19
# Description: A simple flashcard program with a dictionary
#	       taken from King/Yeon's Elementary Korean
######################################################

import os
import sys
import random
from dictionary import dictionary
from readchar import readkey
import keyboard

SCREENWIDTH = 80 

def main():
    if len(sys.argv) != 2:
        usage()
        quit()
    os.system('clear')
    os.system('stty -echo')
    print('\n\n\n\033[1m' + 'Welcome to Korean Flashcards'.center(SCREENWIDTH) + '\033[0m\n\n\n\n\n') 
    sys.stdout.write('\033[5m' + 'Press any key to continue.'.center(SCREENWIDTH) + '\033[0m')
    sys.stdout.flush()
    readkey()
    keyin = ''
    answer = True
    while keyin != 'q':
        if keyin == 'p':
            keyin = ''
            os.system('mpg123 -q ' + card['audio_path'])
            keyin = readkey()
        elif keyin == 'n' and answer == False:
            answer = True
            os.system('clear')
            print('\n\n\n\n\n\n')
            print(card['korean'].center(SCREENWIDTH))
            print('\n\n\n')
            print(card['english'].center(SCREENWIDTH))
            if card['explanation'] != '':
                print(card['explanation'].center(SCREENWIDTH))
            print('\n\n\n\n\n')
            sys.stdout.write('Press p to play audio, q to quit, and any other key to continue.')
            sys.stdout.flush()
            keyin = readkey()
            if keyin == 'n':
                keyin = ''
        elif answer == True: 
            answer = False
            card = get_rand_card()
            os.system('clear')
            print('\n\n\n\n\n\n\n\n\n')
            print(card['korean'].center(SCREENWIDTH))
            print('\n\n\n\n\n')
            sys.stdout.write('p to play audio, n to show answer, q to quit: '.center(SCREENWIDTH))
            sys.stdout.flush()
            keyin = readkey()
        else:
            keyin = readkey()
    os.system('clear')
    os.system('stty echo')

def get_rand_card():
    # if sys.argv[1] == 'all':
    # else:
    try:
        rand_num = random.randint(0,len(dictionary[int(sys.argv[1])-1])-1)
        return (dictionary[int(sys.argv[1])-1])[rand_num]
    except:
        usage()
        quit()
        
def usage():
    print('Usage: flashcardsKtoE.py [Chapter No.]')
    print('e.g.   flashcardsKtoE.py 7')
    print('possible Chapter numbers: 1 2 all')

if __name__ == "__main__":
    main()
