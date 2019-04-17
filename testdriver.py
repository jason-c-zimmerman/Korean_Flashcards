#!/usr/bin/python

####################################################
# testdriver.py: a script for running external tests
####################################################

import random
from dictionary import dictionary

while True:
	rand_card = random.randint(0,len(dictionary[0])-1)
	card = (dictionary[0])[rand_card]
	#if "Is that so?" in card:
	print dictionary[0][rand_card]['english']
