class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []


# Instantiate your villager here
apollo = Villager('Marcus', 'Human', 'Dang Bugs!')

print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 

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

name = Villager('Bones', 'Human', 'bonehead')
print(name.greet_player('Andrew'))

######################################################

