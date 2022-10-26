# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 16:43:34 2022

@author: Nathan
"""

class events:
    
    def light_campfire(item, player):
        player.remove_player_items(item)
        