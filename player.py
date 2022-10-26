# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:15:48 2022

@author: Nathan
"""

class player:
    
    def __init__(self, items = []):
        self.items = items
        
        
    def get_player_items(self):
        return self.items
    
    def add_player_items(self, item):
        self.items.append(item)
        
    def remove_player_items(self, item):
        self.items.remove(item)
