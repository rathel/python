#!/usr/bin/env python3

from roku import Roku
import ssdp
import os

roku = Roku('192.168.11.103')
netflix = roku['Netflix']
plex = roku['Plex']
primevideo = roku['Prime Video']

print('...')

while True:
    actions = input()
    # up
    if(actions == "u"):
        roku.up()
    # down
    elif(actions == "d"):
        roku.down()
    # home
    elif(actions == "h"):
        roku.home()
    # left
    elif(actions == "l"):
        roku.left()
    # right
    elif(actions == "r"):
        roku.right()
    # select
    elif(actions == "s"):
        roku.select()
    # back
    elif(actions == "b"):
        roku.back()
    # play/pause
    elif(actions == "p"):
        roku.play()
    elif(actions == "netflix"):
        netflix.launch()
    elif(actions == "plex"):
        plex.launch()
    elif(actions == "primevideo"):
        primevideo.launch()
    else:
        print("...")
    if actions.strip() == 'exit':
        break
