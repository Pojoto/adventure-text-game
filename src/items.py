import os

#names of all the files in the object_data directory 
filenames = ["normal_items_data.txt", "containers_data.txt", "foods_data.txt"]

'''
The Item class represents a single item in the game.
'''
class Item:
    
    def __init__(self, name, full_name, weight, status, description):
        self.name = name  # a one-word name that serves as a unique identifier
        self.full_name = full_name  # includes adjective
        self.weight = weight  # indicates weight or size
        self.status = status  # a word that describes the status of this item
        self.description = description  # describs the item when examined
    
    def __str__(self):
        result = ''
        count = 0
        for word in self.description.split():
            result += word + ' '
            if count > 65:
                result += '\n'
                count = 0
            else:
                count += len(word) + 1
        return result

class Food(Item):

    def __init__(self, name, full_name, weight, status, description, hp_amount):
        super().__init__(name, full_name, weight, status, description)
        self.hp_amount = hp_amount


class Container(Item):

    def __init__(self, name, full_name, weight, status, description, capacity, contents):
        super().__init__(name, full_name, weight, status, description)
        self.capacity = capacity  
        self.contents = contents  # a list of item names held by this item

#TODOO -- make funciton that can read normal itme files and put it in all below 3 function

def read_foods(objects_dict, foods_file_name):

    with open(foods_file_name, "r") as foods_file:
        name = foods_file.readline().strip()
        while name != '':
            full_name = foods_file.readline().strip()
            weight = int(foods_file.readline().strip())
            status = foods_file.readline().strip()
            description = foods_file.readline().strip()
            hp_amount = int(foods_file.readline().strip())

            objects_dict[name] = Food(name, full_name, weight,
                                        status, description, hp_amount)
            foods_file.readline()
            name = foods_file.readline().strip()

def read_containers(objects_dict, containers_file_name):

    with open(containers_file_name, "r") as containers_file:
        name = containers_file.readline().strip()
        while name != '':
            full_name = containers_file.readline().strip()
            weight = int(containers_file.readline().strip())
            status = containers_file.readline().strip()
            description = containers_file.readline().strip()
            capacity = int(containers_file.readline().strip())
            contents = containers_file.readline().split()
            if contents == "nothing":
                contents = []

            objects_dict[name] = Container(name, full_name, weight,
                                        status, description, capacity, contents)
            containers_file.readline()
            name = containers_file.readline().strip()
            
def read_normal_items(objects_dict, normal_file_name):
    
    with open(normal_file_name, "r") as normal_items_file:

        name = normal_items_file.readline().strip()

        while name != '':
            full_name = normal_items_file.readline().strip()
            weight = int(normal_items_file.readline().strip())
            status = normal_items_file.readline().strip()
            description = normal_items_file.readline().strip()

            objects_dict[name] = Item(name, full_name, weight,
                                        status, description)
            normal_items_file.readline()
            name = normal_items_file.readline().strip()
            
'''
The Items class is a collection of all items in the game.
'''
class Items:
    
    def __init__(self, objects_directory):
        
        self.items_dict = {}  # maps an item name to the corresponding Item object

        path = f"{objects_directory}\\{filenames[0]}"
        read_normal_items(self.items_dict, path)

        path = f"{objects_directory}\\{filenames[1]}"
        read_containers(self.items_dict, path)
        
        path = f"{objects_directory}\\{filenames[2]}"
        read_foods(self.items_dict, path)

        
    def __str__(self):
        return str(self.items_dict)
    
    def get_item(self, item_name):
        return self.items_dict[item_name]

    def get_foods(self):
        foods = set()
        for item in self.items_dict.values():
            if isinstance(item, Food):
                foods.add(item.name)
        return foods

    def get_containers(self):
        containers = set()
        for item in self.items_dict.values():
            if isinstance(item, Container):
                containers.add(item.name)
        return containers

    def get_total_weight(self, items):
        total = 0
        for item_name in items:
            total += self.items_dict[item_name].weight
        return total

