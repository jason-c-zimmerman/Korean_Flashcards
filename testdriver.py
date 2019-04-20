#!/usr/bin/python

####################################################
# testdriver.py: a script for running external tests
####################################################

from curses import wrapper
import time

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
		v = i-10
		stdscr.addstr(i, 0, '10 times by {} is {}'.format(v, 10*v))
		#time.sleep(3)

    stdscr.refresh()
    stdscr.getkey()

print "before wrapper"
wrapper(main)
print "after wrapper"
