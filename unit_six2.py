class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(clues):
    head = clues
    current = clues
    while current:
        if current.next == head:
            return True
        current = current.next
        
    return False

clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue1

print(is_circular(clue1))