# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 10:33:24 2022

@author: Nathan
"""

from encounter import encounter
from events import events
from tools import tools
from locations import locations
from items import items
from interactive_items import interactive_items
from player import player
from scenes import scenes

def sanatize_input(user_input):
    return user_input.strip().lower()

def get_current_location():
    for location in locations:
        if location.get_active():
            print(location.get_description())
            if location.get_first_time():
                location.set_first_time()
                if location.get_description_long() != []:
                    print(location.get_description_long())
            return location
        
def move_location(user_input, current_location, new_locations):
    current_location.set_active(False)
    for new_location in new_locations:
        if new_location[0] == user_input.upper():
            for all_locations in locations:
                if new_location[1] == all_locations.get_id():
                    all_locations.set_active(True)
                    
def display_items(location):
    if location.get_items() != []:
        for item_number in location.get_items():
            item = items[item_number]
            if item.get_hidden() == False:
                print(item.get_location_description())
            
def get_item_by_id(items, _id):
    for item in items:
        if item.get_id() == _id:
            return item
        
def take_all(location):
    location_items = []
    msg = ''
    for item_number in location.get_items():
        item = get_item_by_id(items, item_number)
        if item.get_hidden() == False:
            location_items.append(item_number)
    while location_items != []:
        for item_number in location.get_items():
            item = get_item_by_id(items, item_number)
            if item.get_hidden() == False:
                player.add_player_items(item)
                location.remove_items(item_number)
                location_items.remove(item_number)
                msg += item.get_name() + ' taken.\n'
    if msg == '':
        print("You don't see anything worth taking.\n")
    else:
        print(msg)
            
def take_items(user_input, location):
    current_item = None
    msg = None
    user_input_words = user_input.split(' ')
    for word in user_input_words:
        if location.get_items() != []:
            if len(user_input_words) == 1:
                print('Take what?\n')
            if 'all' in user_input_words:
                current_item = 'all'
            else:
                for item_number in location.get_items():
                    for word in user_input_words:
                        if word in items[item_number].get_alias():
                            if items[item_number].get_hidden() == False:
                                current_item = item_number
        else:
            msg = "You don't see anything worth taking.\n"    
    if msg:
        print(msg)
    elif current_item == 'all':
        take_all(location)
    elif current_item != None:
        item = get_item_by_id(items, current_item)
        if item.get_hidden() == False:
            player.add_player_items(item)
            location.remove_items(current_item)
            print(item.get_name() + ' taken.\n')
    else:
        print("You can't take that.\n")
        
def interact(user_input, location, player):
    
    has_item = False
    iteractive_item_present = False
    correct_item = False
    active_item = []
    usable_item = []
    
    if location.get_interactive_items() != []:
        for word in user_input.split(' '):
            for item in player.get_player_items():
                if word in item.get_alias():
                    has_item = True
                    usable_item = item
                    
        if has_item:
            for word in user_input.split(' '):
                for item_number in location.get_interactive_items():
                    item = get_item_by_id(interactive_items, item_number)
                    if word in item.get_alias():
                        iteractive_item_present = True
                        active_item = item

        if has_item & iteractive_item_present:
            i = get_item_by_id(items, active_item.get_use_with()).get_name()
            if i == usable_item.get_name():
                correct_item = True
            
        if has_item & iteractive_item_present & correct_item:
            if active_item.get_active():
                print("You've already done that.")
            else:
                active_item.set_active(True)
                for item_number in location.get_items():
                    item = get_item_by_id(items, item_number)
                    item.set_hidden(False)
                print(active_item.get_description())
                events.light_campfire(get_item_by_id(items, 0), player)
            
        else:
            print("You can't do that.\n")
    
                               
active = True
player = player()
locations[0].set_active(True)
scenes.intro()               

while (active):
    
    directions = ['n', 'north', 's', 'south', 'e', 'east', 'w', 'west']
    command_look = ['l', 'look', 'see', 'description']
    command_take = ['t', 'take', 'get', 'grab', 'pickup']
    command_interact = ['u', 'use']
    command_inventory = ['i', 'inv', 'inventory']
    command_quit = ['q', 'quit']
    command_help = ['h', 'help', '?']
    
    location = get_current_location()
    if location.interactive_items != []:
        for item_number in location.interactive_items:
            item = get_item_by_id(interactive_items, item_number)
            if item.get_active():
                print(item.get_active_description())
            
    display_items(location)
    
    print('')
    user_input = sanatize_input( input(location.get_name() + ": ") )
    print('')
    
    user_input_words = user_input.split(' ')
    
    if user_input in command_look:
        tools.type_text('Look: ' + location.get_description_long())
        
    elif user_input_words[0] in command_take:
        take_items(user_input, location)
        
    elif user_input_words[0] in command_interact:
        interact(user_input, location, player)

    elif user_input in directions:
        if location.move(user_input):
            new_locations = location.get_adjacent_locations()
            move_location(user_input, location, new_locations)
            encounter.check_encounter()
        else:
            print("You can't go that way.")
    
            
    elif user_input in command_inventory:
        print('INVENTORY: ')
        inv = ''
        for item in player.get_player_items():
            inv += " - " + item.get_name() + ": " + item.get_description() + '\n'
        if inv != '':
            print(inv)
        else:
            print(' - Your pockets are empty..\n')
        
        
    elif user_input in command_help:
        scenes.print_help()
         
    elif user_input in command_quit:
        user_quit = input("Are you sure you want to quit? (y/n): ").lower()
        if user_quit == 'y' or user_quit == 'yes':
            active = False
            
    else:
        print('Unknown command')
        
    if player.get_health() <= 0:
        print('Sadly you have died.  Maybe use should think about your mistakes.')
        active = False

