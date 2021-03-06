"""
Filename: iteminventory.py
Description: Defines an item and inventory class to be used in adventure game
(see README.md of project directory)
Author: Lauren K. Scott
"""

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    # getter method to return item's name
    def get_name(self):
        return self.name
    
    # getter method to safely retrieve item description
    def get_description(self):
        return self.description
    

class Obstacle(Item):
    def __init__(self, name, description, weakness, unlock):
        Item.__init__(self, name, description)
        #defines the item that will defeat obstacle
        self.weakness = weakness
        #the item or next obstacle that is revealed upon defeat
        self.unlock = unlock
        #a message to display to the player when they defeat an obstacle
        self.defeat_message = None

    def defeat(self, item_name):
        if self.weakness == 'view' and item_name == 'view':
            print(self.defeat_message)
            return True
        elif item_name == self.weakness.get_name():
            print(self.defeat_message)
            return True
        return False
        
class Inventory:
    def __init__(self):
        # dictionary of items. key is item name, val is actual item object
        self.items_by_name = {}

    # check if a given item is in the inventory by looking it up in items_by_name dictionary
    def in_inventory(self, item_name):
        if item_name in self.items_by_name:
            return True
        return False

    def add_item(self, item):
        #if item not already in inventory, add it
        if not self.in_inventory(item):
            self.items_by_name[item.get_name()] = item
        return self.items_by_name

    def rem_item(self, item_name):
        #if item is in inventory, delete it
        if self.in_inventory(item_name):
            del items_by_name[item_name]
        return self.items_by_name

    def describe_all(self):
        # if items_by_name is not empty
        if self.items_by_name:
            # print each item description on a seperate line
            for item in self.items_by_name.values():
                print(item.get_description())
        else:
            print("Your inventory is empty.")
        return self.items_by_name
    

#Initialize items in game, grouped by tile
all_items = Inventory()
#tile0
rock = Item('rock', 'a jagged black rock, perhaps flint')
all_items.add_item(rock)
#tile3
shovel = Item('shovel', 'a small shovel')
all_items.add_item(shovel)
grave = Obstacle('grave', 'what appears to be a shallow grave',\
     'view', shovel)
grave.defeat_message = 'Thankfully, the grave is empty. Inside the grave, a well-worn shovel.'
all_items.add_item(grave)
#tile6
axe = Item('axe', 'a rusted old axe, covered in barnacles')
all_items.add_item(axe)
boat = Obstacle('boat', 'the remains of a small boat', 'view', axe)
boat.defeat_message = '''The dinghy was ravaged not by the stormy waters, but by man. \
    A message was hacked into the splintered bow: "Wickies heed not the siren call". You see an axe lying on the dock.'''
all_items.add_item(boat)
#tile5
bread = Item('bread', 'some soggy old bread')
all_items.add_item(bread)
rations = Obstacle('crate', 'a wooden crate labelled "EMERGENCY RATIONS"',\
    shovel, bread)
rations.defeat_message = 'You excitedly open the crate, only to find a few crumbs of bread, too soggy even for you to eat.'
all_items.add_item(rations)
#tile2
cotton = Item('cotton', 'scraps of cotton from an old sailor\'s coat')
all_items.add_item(cotton)
nest = Obstacle('nest', 'a strange looking nest',
 'view', cotton)
nest.defeat_message = 'As you approach, you see that the nest is made up of the cotton scraps from an old sailor\'s coat.'
all_items.add_item(nest)
bird = Obstacle('bird', 'a crippled old gull guarding its nest',\
    bread, nest)
bird.defeat_message = '''You scatter the crumbs over the ground. \
    The gull hops down to eat them, then glances back at you before flying away. '''
all_items.add_item(bird)
#tile4
key = Item('key', 'a large key on a silver chain')
all_items.add_item(key)
medusa = Obstacle('medusa', 'a fearsome creature with eels for hair', axe, key)
all_items.add_item(medusa)
medusa.defeat_message = '''Charging forward into the surf, you swing wildly at the creature with your axe. \
    Suddenly, her form changes again, and you see that you are wrestling with a mass of seaweed and fishing nets.\
        Among the tangled mass is a glimmering metal key'''
mermaid = Obstacle('mermaid', 'a beautiful woman with the voice of an angel',\
    cotton, medusa)
mermaid.defeat_message = '''You tear off two strips of cotton and stuff them into your ears. Realizing that her song cannot sway you, \
    the mermaid's face twists into a horrifying snarl. Her beauty is gone, replaced by a hideous sea-witch.'''
all_items.add_item(mermaid)
#tile7
code = Item('code', 'a slip of paper that says: 9VK0A')
all_items.add_item(code)
book = Obstacle('book', 'a ragged book labelled "CAPTAIN\'S LOG"', 'view', code)
all_items.add_item(book)
shack = Obstacle('shack', 'the dusty interior of a one-room shack', 'view', book)
all_items.add_item(shack)
door = Obstacle('door', 'a locked door', key, shack) 
all_items.add_item(door)
#tile8
oil = Item('oil', 'a full canister of oil')
all_items.add_item(oil)
#tile10
unlit_wick = Obstacle('wick', 'the wick needs a spark to ignite', rock, unlock=None)
all_items.add_item(unlit_wick)
empty_tank = Obstacle('tank', 'the fuel tank is empty', oil, unlit_wick)
all_items.add_item(empty_tank)
hatch = Obstacle('hatch', 'a keypad to unlock the hatch', code, empty_tank)
all_items.add_item(hatch)
#tile9
carving =Item('carving', 'carved into the otherwise smooth wall is a \
    verse: "blah blah"')
all_items.add_item(carving)
#Initialize player inventory that is empty
player_inv = Inventory()
