# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 11:14:49 2022

@author: Nathan
"""

from location import location

locations = [
    
    location(0,
            "Unknown location",
            "You haven't been here before",
            "This location is not familiar, or maybe it is, you find it hard to remember..  \nA path leads to the South.",
            ['S'],
            [['S', 1]]),

    location(1,
            "A dark forest",
            "You are in a dark, dark forest",
            "You've definitely been here before, at least, maybe?  \nA path leads to the North and South",
            ['N', 'S'],
            [['N', 0],['S', 2]],
            items = [0, 1]),

    location(2,
            "A shady clearing",
            "The forest gets a little lighter.",
            "You look up and see a partially full moon through the trees. \nA path leads to the North and South",
            ['N', 'S'],
            [['N', 1],['S', 3]]),
    
    location(3,
            "A ruined campsite",
            "Remenants of a campsite, somethings torn this place apart.",
            "A collapsed tent sits toward the edge of the site.\nThere's a fire pit with wood still smouldering. \nA path leads to the North and South",
            ['N', 'S'],
            [['N', 2], ['S', 4]],
            items = [2],
            interactive_items = [0]),
            
    location(4,
            "Campsite perimeter",
            "A campsite sits off in the distance.",
            "The path comes to a four way fork. \nA paths North, South, East, and West",
            ['N', 'S', 'E', 'W'],
            [['N', 3],['S', 5], ['E', 6], ['W', 7]]),
    
    location(5,
            "Campsite perimeter - South",
            "A campsite sits off in the distance.",
            "The path comes to a four way fork. \nA paths North, South, East, and West",
            ['N'],
            [['N', 4]]),
    
    location(6,
            "Campsite perimeter - East",
            "A campsite sits off in the distance.",
            "The path comes to a four way fork. \nA paths North, South, East, and West",
            ['W'],
            [['W', 4]]),
    
    location(7,
            "Campsite perimeter - West",
            "A campsite sits off in the distance.",
            "The path comes to a four way fork. \nA paths North, South, East, and West",
            ['E'],
            [['E', 4]]),
            
]