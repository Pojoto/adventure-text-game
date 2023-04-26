
class Player:
    
    def __init__(self, name):
        self.name = name
        self.max_capacity = 5
        self.health = 100
        self.inventory = set()
    
    def change_capacity(self, capacity):
        self.capacity = capacity
    
    def take_damage(self, damage):
        self.health = self.health - damage
        print(f"Took {damage} damage.")
        if self.health <= 0:
            print("YOU DEAD!")
            
    
    def gain_health(self, amount):
        self.health = self.health + amount
        if self.health > 100:
            amount = amount - (self.health - 100)
            self.health = 100
        print(f"Gained {amount} health.")
    
    def add_item(self, item):
        self.inventory.add(item)
    
    def remove_item(self, item):
        self.inventory.remove(item)
    
    def can_take_item(self, item, items_object):
        if items_object.get_total_weight(self.inventory) + item.weight > self.max_capacity:
            return False
        return True
    
    def process_inventory(self, items_object):
        if len(self.inventory) == 0:
            print("You're not carrying anything.")
        else:
            print('You are currently carrying:')
            for item_name in self.inventory:
                item = items_object.get_item(item_name)
                print('   ' + item.full_name)
            