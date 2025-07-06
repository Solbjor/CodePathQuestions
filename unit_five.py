
######################################################

# Test behavior to make sure its what you want, in Test Driven Development (or Behavior Driven Development)

######################################################
class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
        
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
        
def of_personality_type(townies, personality_type):
    matches = []
    for townie in townies:
        if townie.personality == personality_type:
            matches.append(townie.name)
    return matches

def message_received(start_villager, target_villager):
    current = start_villager
    while current:
        if current.neighbor == target_villager:
            return True
        else:
            current = current.neighbor
    return False
             

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))

#apollo = Villager('Apollo', 'Eagle', 'pah')

###print(apollo.name)  
#print(apollo.species)  
#print(apollo.catchphrase) 
#print(apollo.furniture) 

#bones = Villager('Bones', 'Dog', 'yip yip')
#print(bones.greet_player('Andrew'))

#bones.catchphrase = "ruff it up"
#print(bones.greet_player('Andrew'))

#alice = Villager("Alice", "Koala", "guvnor")

#alice.set_catchphrase("sweet dreams")
#print(alice.catchphrase)
#alice.set_catchphrase("#?!")
#print(alice.catchphrase)

#alice = Villager("Alice", "Koala", "guvnor")
#print(alice.furniture)

#alice.add_item("acoustic guitar")
#print(alice.furniture)

#alice.add_item("cacao tree")
#print(alice.furniture)

#alice.add_item("nintendo switch")
#print(alice.furniture)

#alice = Villager("Alice", "Koala", "guvnor")

#alice.print_inventory()

#alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
#alice.print_inventory()

#isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
#bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
#stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

#print(of_personality_type([isabelle, bob, stitches], "Lazy"))
#print(of_personality_type([isabelle, bob, stitches], "Cranky"))

################################################################################

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
tom_nook = Node("Tom Nook")
tommy = Node("Tommy") 
tom_nook.next = tommy 
timmy = Node("Timmy")
tom_nook.next = timmy
timmy.next = tommy
print(tom_nook.value)
print(tom_nook.next.value)
print(timmy.value)
print(timmy.next.value)
print(tommy.value)
print(tommy.next)