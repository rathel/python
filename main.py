#!/usr/bin/env python3

from roku import Roku
import ssdp
import os

roku = Roku('192.168.11.103')
netflix = roku['Netflix']

print('...')

while True:
    actions = input()
    if(actions == "up"):
        roku.up()
    elif(actions == "down"):
        roku.down()
    elif(actions == "home"):
        roku.home()
    elif(actions == "left"):
        roku.left()
    elif(actions == "right"):
        roku.right()
    elif(actions == "select"):
        roku.select()
    elif(actions == "netflix"):
        netflix.launch()
    else:
        print("...")
    if actions.strip() == 'exit':
        break
