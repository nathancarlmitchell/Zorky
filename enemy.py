# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:15:48 2022

@author: Nathan
"""

import random

class enemy:
    
    def __init__(self, name, location, enemies = [], health = 10):
        self.enemies = enemies
        self.name = name
        self.health = health
        self.location = location
        
        
    def get_location(self):
        return self.location

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

    