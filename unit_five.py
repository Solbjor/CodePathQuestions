
######################################################

# Test behavior to make sure its what you want, in Test Driven Development (or Behavior Driven Development)

######################################################
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
        
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20:
            words = new_catchphrase.split()
            for word in words:
                if not word.isalpha():
                    print("Invalid catchphrase")
                    return
            self.catchphrase = new_catchphrase
            print("Catchphrase updated")
        else:
            print("Invalid catchphrase")
    
    def add_item(self, item_name):
        valid_names = ["acoustic guitar", "ironwood kitchenette","rattan armchair", "kotatsu", "cacao tree"]
        if item_name in valid_names:
            self.furniture.append(item_name)

    def print_inventory(self):
        if self.furniture == []:
            print("Inventory Empty")
        furniture_frequency = {}
        for furniture in self.furniture:
            if furniture in furniture_frequency:
                furniture_frequency[furniture] += 1 
            else: 
                furniture_frequency[furniture] = 1
        for key, value in furniture_frequency.items():
            print(f"{key}: {value}")
        

apollo = Villager('Apollo', 'Eagle', 'pah')

print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 

bones = Villager('Bones', 'Dog', 'yip yip')
print(bones.greet_player('Andrew'))

bones.catchphrase = "ruff it up"
print(bones.greet_player('Andrew'))

alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)

alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)

alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()
