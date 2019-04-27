#!/usr/bin/python
# -*- coding: utf-8 -*-

######################################################
# Title: KtoE.py
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
from playsound import playsound
#import getopt #TODO make the args opts
import curses
import locale

locale.setlocale(locale.LC_ALL, '')
# try block is for cross-platform functionality
try:
	reload(sys)
	sys.setdefaultencoding('utf8')
except:
	pass

stdscr = None

def main(scr):
    global stdscr
    stdscr = scr
    numlines = curses.LINES
    numcols = curses.COLS
    curses.curs_set(0)
    stdscr.clear()

    if len(sys.argv) < 2 or len(sys.argv) > 3:
        usage()
        sys.exit(2)

    system='unix'
    if len(sys.argv) == 3 and sys.argv[2] == 'm':
        system='android'

    stdscr.addstr(int(numlines/2)-2, 0, 'Welcome to Korean Flashcards'.center(numcols), curses.A_BOLD)
    stdscr.addstr(int(numlines/2)+1, 0, 'Press any key to continue.'.center(numcols), curses.A_BLINK)
    stdscr.getkey()

    keyin = 'n'
    answer = False
    deck = []

    while keyin != 'q':
        resized = curses.is_term_resized(numlines, numcols)
        if resized:
            numlines, numcols = stdscr.getmaxyx()
            stdscr.clear()
            curses.resizeterm(numlines, numcols)
            stdscr.refresh()

        if keyin == 'p':
        # Play sound
            keyin = ''
            if system == 'unix':
                playsound(card['audio_path'])
            elif system == 'android':
                os.system('play-audio ' + card['audio_path'])
            keyin = stdscr.getkey()
        elif keyin == 'n' and answer:
        # Show answer
            stdscr.clear()
            stdscr.refresh()
            answer = False
            stdscr.addstr(int(numlines/2)-2, 0, card['korean'].center(numcols))
            stdscr.addstr(int(numlines/2)+1, 0, card['english'].center(numcols))
            if card['explanation'] != '':
                stdscr.addstr(int(numlines/2)+3, 0, card['explanation'].center(numcols))
            stdscr.addstr(numlines-2, 0, 'p audio, n next, q quit'.center(numcols))
            keyin = stdscr.getkey()
        elif keyin == 'n' and not answer:
        # Show next question
            stdscr.clear()
            stdscr.refresh()
            answer = True
            deck = get_rand_card(deck)
            card = deck.pop(0)
            stdscr.addstr(int(numlines/2), 0, card['korean'].center(numcols))
            stdscr.addstr(numlines-2, 0, 'p audio, n ans, q quit'.center(numcols))
            keyin = stdscr.getkey()
        else:
            keyin = stdscr.getkey()
		

#def pad_string(string, numcols):
#    # Pad string text with appropriate spaces
#    len_string = len(string)
#    if numcols % 2 == 0:
#        if len_string % 2 == 0:
#            for i in range(int((numcols-len_string)/2)): string = u'\u2001' + string 
#            for i in range(int((numcols-len_string)/2)): string = string + u'\u2001' 
#        else: # len_string % 2 == 1
#            for i in range(int((numcols-len_string)/2)): string = u'\u2001' + string
#            for i in range(int((numcols-len_string)/2+1)): string = string + u'\u2001' 
#    else: # numcols % 2 == 1
#        if len_string % 2 == 0:
#            for i in range(int((numcols-len_string)/2)): string = u'\u2001' + string
#            for i in range(int((numcols-len_string)/2+1)): string = string + u'\u2001'
#        else: # len_string % 2 == 1 
#            for i in range(int((numcols-len_string)/2+1)): string = u'\u2001' + string
#            for i in range(int((numcols-len_string)/2+1)): string = string + u'\u2001'
#    return string


def get_rand_card(deck):
	if len(deck) == 0:
		try:
		    if sys.argv[1] == 'all':
			    for d in dictionary:
				    deck += d
		    else:
			    deck = list(dictionary[int(sys.argv[1])-1])
		except:
			usage()
			sys.exit(2)
		
	idx = random.randint(0,(len(deck))-1)
	card = deck[idx]
	deck.remove(card)
	deck.insert(0,card)
	return deck
        
def usage():
	stdscr.addstr(0,0,'usage: flashcardsKtoE.py CHAPTER# [m(obile)]')
	stdscr.addstr(1,0,'e.g.   flashcardsKtoE.py 1 m')
	stdscr.addstr(2,0,'possible Chapter numbers: 1 2 all')
	stdscr.refresh()
	stdscr.getkey()

if __name__ == "__main__":
    curses.wrapper(main)
