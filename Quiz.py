#!/usr/bin/python
# -*- coding: utf-8 -*-

######################################################
# Title: Quiz:.py
# Author: Jason C Zimmerman
# Date: 4/16/19
# Description: A simple quiz program with a dictionary
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
reload(sys)
sys.setdefaultencoding('utf8')

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

	stdscr.addstr(int(numlines/2)-2, 0, 'Welcome to Korean Quiz'.center(numcols), curses.A_BOLD) 
	stdscr.addstr(int(numlines/2)+1, 0, 'Press any key to continue.'.center(numcols), curses.A_BLINK)
	stdscr.getkey()

	answer = False
	counter = 0
	correct = 0
	keyin = ''
	str_in = ''
	deck = []

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
			if system == 'unix':
				playsound(card['audio_path'])
			elif system == 'android':
				os.system('play-audio ' + card['audio_path'])
			keyin = stdscr.getkey()
		elif answer:
		# Show answer
			stdscr.clear()
			stdscr.refresh()
			answer = False
			stdscr.addstr(int(numlines/2)-2, 0, card['english'].center(numcols))
			curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
			stdscr.addstr(int(numlines/2)+1, 0, card['korean'].center(numcols), curses.color_pair(1) | curses.A_BOLD)
			stdscr.addstr(int(numlines/2)+3, 0, str_in.center(numcols))
			stdscr.addstr(numlines-2, 0, 'Were you correct? (y/n): '.center(numcols))
			while keyin != r'[yn]':# or keyin != 'n':
				keyin = stdscr.getkey()	
				if keyin == 'y':
					correct += 1
					counter += 1
					break
				if keyin == 'n':
					counter += 1
					break
			stdscr.addstr(numlines-2, 0, 'p audio, q quit, any next'.center(numcols))
			keyin = stdscr.getkey()
		elif not answer:
		# Show next question
			stdscr.clear()
			stdscr.refresh()
			answer = True
			deck = get_rand_card(deck)
			card = deck.pop(0)
			stdscr.addstr(int(numlines/2)-2, 0, card['english'].center(numcols))
			stdscr.addstr(int(numlines/2)-6, 0, ('Question Number ' + str(counter + 1)).center(numcols))
			stdscr.addstr(int(numlines/2)+1, 0, ('Answer: ' + " ".ljust(len(card['korean']))).center(numcols))
			curses.echo()
			curses.curs_set(1)
			stdscr.move(int(numlines/2)+1, (numcols - len('Answer: ') - len(card['korean'])) / 2 + len('Answer: '))
			curses.doupdate()
			str_in = stdscr.getstr()
			curses.noecho()
			curses.curs_set(0) 
		else:
			keyin = stdscr.getkey()

	stdscr.clear()
	stdscr.refresh()
	message1 = 'You got ' + str(correct) + ' out of ' + str(counter) + ' correct.'
	message2 = str(int(float(correct)/counter*100)) + '%'
	stdscr.addstr(int(numlines/2)-1, 0, message1.center(numcols))
	stdscr.addstr(int(numlines/2)+1, 0, message2.center(numcols))
	stdscr.getkey()

#def pad_string(string, numcols):
#    # Pad string text with appropriate spaces
#    len_string = len(string)
#    if numcols % 2 == 0:
#        if len_string % 2 == 0:
#            for i in range((numcols-len_string)/2): string = u'\u2001' + string 
#            for i in range((numcols-len_string)/2): string = string + u'\u2001' 
#        else: # len_string % 2 == 1
#            for i in range((numcols-len_string)/2): string = u'\u2001' + string
#            for i in range((numcols-len_string)/2+1): string = string + u'\u2001' 
#    else: # numcols % 2 == 1
#        if len_string % 2 == 0:
#            for i in range((numcols-len_string)/2): string = u'\u2001' + string
#            for i in range((numcols-len_string)/2+1): string = string + u'\u2001'
#        else: # len_string % 2 == 1 
#            for i in range((numcols-len_string)/2+1): string = u'\u2001' + string
#            for i in range((numcols-len_string)/2+1): string = string + u'\u2001'
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
	stdscr.addstr(0,0,'Usage: flashcardsKtoE.py CHAPTER# [m(obile)]')
	stdscr.addstr(1,0,'e.g.   flashcardsKtoE.py 1 m')
	stdscr.addstr(2,0,'possible Chapter numbers: 1 2 all')
	stdscr.refresh()
	stdscr.getkey()

if __name__ == "__main__":
    curses.wrapper(main)
