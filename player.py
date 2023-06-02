# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:15:48 2022

@author: Nathan
"""

class player:
    
    def __init__(self, items = []):
        self.items = items
        self.health = 100
        
        
    def get_player_items(self):
        return self.items
    
    def add_player_items(self, item):
        self.items.append(item)
        
    def remove_player_items(self, item):
        self.items.remove(item)

    def get_health(self):
        return self.health
    
    def update_health(self, change):
        self.health = self.health + change
        
    def print_health(self):
        if self.health >= 100:
            print("You've never felt this good before.. At least physically.\n")
        elif self.health >= 75:
            print("You've taken a few hits but you're used to it by now.\n")
        elif self.health >= 50:
            print("You don't looks so great..  You don't feel so great either.\n")
        elif self.health >= 25:
            print("You won't last at this rate.\n")
        else:
            print("Goodbye cruel world.\n")
    