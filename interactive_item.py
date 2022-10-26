# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:47:31 2022

@author: Nathan
"""

class interactive_item:
           
    def __init__(self, _id, name, description, use_with, alias = [],
                 active = False, active_description = []):   
        
        self._id = _id
        self.name = name
        self.description = description
        self.alias = alias
        self.use_with = use_with
        self.active = active
        self.active_description = active_description
        
    def get_id(self):
        return self._id
        
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_alias(self):
        return self.alias
    
    def get_use_with(self):
        return self.use_with
    
    def get_active(self):
        return self.active
    
    def set_active(self, active):
        self.active = active
    
    def get_active_description(self):
        return self.active_description