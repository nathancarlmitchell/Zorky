# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 09:56:05 2021

@author: Nathan Mitchell, Ben Rome - McAllen Solutions, Frankfort KY
"""

#from locations import locations

class location:
    
    def __init__(self, _id, name, description, description_long,
                 directions, adjacent_locations, items = [],
                 interactive_items = [], first_time = True,
                 enemies_present = False):
        
        self.first_time = True
        self._id = _id
        self.name = name
        self.description = description
        self.description_long = description_long
        self.directions = directions
        self.active = False
        self.adjacent_locations = adjacent_locations
        self.items = items
        self.interactive_items = interactive_items
        self.enemies_present = enemies_present
        
        
    def get_first_time(self):
        return self.first_time
    
    def set_first_time(self):
        self.first_time = False
        
    def get_id(self):
        return self._id
        
    def get_active(self):
        return self.active
    
    def set_active(self, active):
        self.active = active
        
    def get_name(self):
        return f"{self.name}"

    def get_description(self):
        return f"{self.description}"
    
    def get_description_long(self):
        return f"{self.description_long}"
    
    def get_adjacent_locations(self):
        return self.adjacent_locations
    
    def get_items(self):
        return self.items
    
    def get_interactive_items(self):
        return self.interactive_items
    
    def remove_items(self, item):
        self.items.remove(item) 
        
    def get_enemies_present(self):
        return self.enemies_present
    
    def move(self, direction):
        if direction.upper() in self.directions:
            return True
        else:
            return False