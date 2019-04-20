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
from playsound import playsound
#import getopt #TODO make the args opts
import curses
import locale

locale.setlocale(locale.LC_ALL, '')

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
	
	SYSTEM='unix'
	if len(sys.argv) == 3 and sys.argv[2] == 'm':
		SYSTEM='android'

	stdscr.addstr(int(numlines/2)-1, 0, 'Welcome to Korean Flashcards'.center(numcols), curses.A_BOLD) 
	stdscr.addstr(int(numlines/2)+1, 0, 'Press any key to continue.'.center(numcols), curses.A_BLINK)
	stdscr.getkey()

	keyin = 'n'
	answer = True

	while keyin != 'q':
        # Check if screen was re-sized
        resized = curses.is_term_resized(numlines, numcols)
        if resized:
            numlines, numcols = stdscr.getmaxyx()
            stdscr.clear()
            curses.resizeterm(numlines, numcols)
            stdscr.refresh()

		if keyin == 'p':
		# Play sound
			keyin = ''
			if SYSTEM == 'unix':
				playsound(card['audio_path'])
			elif SYSTEM == 'android':
				os.system('play-audio ' + card['audio_path'])
			keyin = stdscr.getkey()
		elif keyin == 'n' and not answer:
		# Show answer
			stdscr.clear()
			stdscr.refresh()
			answer = True
			stdscr.addstr(int(numlines/2)-1, 0, card['english'].center(numcols))
			stdscr.addstr(int(numlines/2)+1, 0, card['korean'].center(numcols))
			if card['explanation'] != '':
				stdscr.addstr(int(numlines/2)+1, 0, card['explanation'].center(numcols))
			stdscr.addstr(numlines-2, 0, 'p audio, n next, q quit'.center(numcols))
			keyin = stdscr.getkey()
		elif keyin == 'n' and answer:
		# Show next question
			stdscr.clear()
			stdscr.refresh()
			answer = False
			card = get_rand_card()
			stdscr.addstr(int(numlines/2), 0, card['english'].center(numcols))
			stdscr.addstr(numlines-2, 0, 'n ans, q quit'.center(numcols))
			keyin = stdscr.getkey()
			if keyin == 'p':
				keyin = ''
		else:
			keyin = stdscr.getkey()


def get_rand_card():
	try:
		if sys.argv[1] == 'all':
			rand_chap= random.randint(0,len(dictionary)-1)
			rand_card = random.randint(0,len(dictionary[rand_chap])-1)
			return (dictionary[rand_chap])[rand_card]
		else:
			chap = int(sys.argv[1])-1
			rand_card = random.randint(0,len(dictionary[chap])-1)
			return (dictionary[chap])[rand_card]
	except:
		usage()
		os.system('stty echo')
		sys.exit(2)
        
def usage():
	stdscr.addstr(0,0,'Usage: flashcardsKtoE.py CHAPTER# [m(obile)]')
	stdscr.addstr(0,0,'e.g.   flashcardsKtoE.py 1 m')
	stdscr.addstr(0,0,'possible Chapter numbers: 1 2 all')
	stdscr.refresh()
	stdscr.getKey()

if __name__ == "__main__":
    curses.wrapper(main)
