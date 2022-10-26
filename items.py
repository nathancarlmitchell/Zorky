# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 16:53:44 2022

@author: Nathan
"""

from item import item

items = [
        
    item(0, "matchbook",
         "A damp old match book.",
         "A damp old match book.  Looks like there's one match left.",
         ['matchbook', 'matches', 'match']),
    
    item(1, "knife",
         "A small pocketknife",
         "A bloody knife sits in a pile of brush.",
         ['knife']),
    
    item(2, "key",
         "A small silver key.",
         "A glint of something shiny catches your eye.\nThe fire reflects off of a small silver key laying in the dirt.",
         ['key'],
         hidden = True)
    
    ]