# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 16:51:56 2022

@author: Nathan
"""

class item:
           
    def __init__(self, _id, name, description, location_description,
                 alias = [],
                 hidden = False):  
        
        self._id = _id
        self.name = name
        self.description = description
        self.location_description = location_description
        self.alias = alias
        self.hidden = hidden
        
    def __del__(self):
        pass
        
    def get_id(self):
        return self._id
        
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_location_description(self):
        return self.location_description
    
    def get_alias(self):
        return self.alias
        
    def get_hidden(self):
        return self.hidden    
    
    def set_hidden(self, hidden):
        self.hidden = hidden
        

