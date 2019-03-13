#!/usr/bin/env python3

from roku import Roku
import ssdp
import os
import curses

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

roku = Roku('192.168.11.103')
netflix = roku['Netflix']
plex = roku['Plex']
primevideo = roku['Prime Video']

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_RIGHT:
            roku.right()
        elif char == curses.KEY_LEFT:
            roku.left()
        elif char == curses.KEY_UP:
            roku.up()
        elif char == curses.KEY_DOWN:
            roku.down()
        elif char == curses.KEY_BACKSPACE:
            roku.back()
        elif char == 10:
            roku.select()
        elif char == ord('p'):
            roku.play()
        elif char == ord('h'):
            roku.home()
        elif char == ord('b'):
            roku.back()
finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()

