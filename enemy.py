# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:15:48 2022

@author: Nathan
"""

import random

class enemy:
    
    def __init__(self, enemies = [], health = 10):
        self.enemies = enemies
        self.health = health
        
        
    def get_enemies(self):
        return self.items
    
    def add_enemies(self, enemy):
        self.items.append(enemy)
        
    def remove_enemies(self, enemy):
        self.items.remove(enemy)    

    def get_health(self):
        return self.health
    
    def update_health(self, change):
        self.health = self.health + change
        if self.health <= 0:
            self.remove_enemies(self)
        
    def attack(self):
        chance = random.randint(1, 2)
        if (chance <= 1):
            print('hit')

    