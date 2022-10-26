# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 16:14:28 2022

@author: Nathan
"""

from tools import tools

class scenes:
    
    def intro():
        tools.type_text("You wake up from a deep, deep sleep.")
        tools.type_text("Your eyes slowly adjust to the dim lighting around you.")
        tools.type_text("The air feels cold and damp.")
        tools.type_text("You touch the back of your head, it throbs with pain.")
        tools.type_text("'What happened?'")
        tools.type_text("You struggle to remember how you ended up here but all you can think about is the pain radiating from the base of your skull.")
        tools.type_text("You sit for a momenent and collect yourself.")
        tools.type_text("You get up to your feet slowly.")
        tools.type_text("")
        tools.type_text(" -- Type help for commands -- ")
        tools.type_text("")
        
    def print_help():
        print('')
        print('COMMANDS: \n LOOK - L\n TAKE -T\n INVENTORY - I\n USE - U\n HELP - H\n QUIT - Q\n')
        print('Directions: \n NORTH - N\n SOUTH - S\n EAST - E\n WEST - W\n')
        print('')