# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:15:48 2022

@author: Nathan
"""

import random
import enemy

class encounter:
    
    def __init__(self):
        pass
    
    def check_encounter():
        chance = random.randint(1, 100)
        if chance <= 21:
            print('1/5')
            enemy()
        
        
    
    