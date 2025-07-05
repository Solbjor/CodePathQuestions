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