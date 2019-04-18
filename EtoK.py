#!/usr/bin/python
# -*- coding: utf-8 -*-

######################################################
# Title: Korean_Flashcards.py
# Author: Jason C Zimmerman
# Date: 4/16/19
# Description: A simple flashcard program with a dictionary
#	       taken from King/Yeon's Elementary Korean
######################################################

# TODO: debug sound support for mobile

import os
import sys
import random
from dictionary import dictionary
from readchar import readkey
import keyboard
from playsound import playsound
#import getopt #TODO make the args opts

def main():
	if len(sys.argv) < 2 or len(sys.argv) > 3:
		usage()
		sys.exit(2)
	SCRWID = 80 
	SYSTEM='unix'
	if len(sys.argv) == 3 and sys.argv[2] == 'm':
		SCRWID = 24
		SYSTEM='android'
	try:
		os.system('clear')
		os.system('stty -echo')
		print('\n\n\n\033[1m' + 'Welcome to Korean Flashcards'.center(SCRWID) + '\033[0m\n\n\n\n\n') 
		sys.stdout.write('\033[5m' + 'Press any key to continue.'.center(SCRWID) + '\033[0m')
		sys.stdout.flush()
		readkey()
		keyin = 'n'
		answer = True

		while keyin != 'q':
			if keyin == 'p':
			# Play sound
				keyin = ''
				if SYSTEM == 'unix':
					playsound(card['audio_path'])
				elif SYSTEM == 'android':
					os.system('play-audio ' + card['audio_path'])
				keyin = readkey()
			elif keyin == 'n' and not answer:
			# Show answer
				answer = True
				os.system('clear')
				print('\n\n\n\n\n\n')
				print(card['english'].center(SCRWID))
				print('\n\n\n')
				print(card['korean'].center(SCRWID))
				if card['explanation'] != '':
					print(card['explanation'].center(SCRWID))
				print('\n\n\n\n\n')
				sys.stdout.write('p audio, n next, q quit'.center(SCRWID))
				sys.stdout.flush()
				keyin = readkey()
			elif keyin == 'n' and answer:
			# Show next question
				answer = False
				card = get_rand_card()
				os.system('clear')
				print('\n\n\n\n\n\n\n\n\n')
				print(card['english'].center(SCRWID))
				print('\n\n\n\n\n')
				sys.stdout.write('p audio, n ans, q quit'.center(SCRWID))
				sys.stdout.flush()
				keyin = readkey()
			else:
				keyin = readkey()
		os.system('clear')
		os.system('stty echo')
	except:
		os.system('clear')
		os.system('stty echo')
		sys.exit(2)

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
    print('Usage: flashcardsKtoE.py CHAPTER# [m(obile)]')
    print('e.g.   flashcardsKtoE.py 1 m')
    print('possible Chapter numbers: 1 2 all')

if __name__ == "__main__":
    main()
