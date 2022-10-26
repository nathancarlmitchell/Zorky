# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:14:22 2022

@author: Nathan
"""
import time

class tools:
    
    def type_text(text):
        for letter in text:
            print(letter, end = "")
            time.sleep(0.00)
        print("\n")
        