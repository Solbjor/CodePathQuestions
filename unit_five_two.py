# # # # class Node:
# # # #     def __init__(self, value, next=None):
# # # #         self.value = value
# # # #         self.next = next

# # # # # For testing
# # # # def print_linked_list(head):
# # # #     current = head
# # # #     while current:
# # # #         print(current.value, end=" -> " if current.next else "\n")
# # # #         current = current.next

# # # # def halve_list(head):
# # # #     current = head
# # # #     while current:
# # # #         current.value = current.value / 2
# # # #         current = current.next
        
# # # #     return head

# # # # node_one = Node(5)
# # # # node_two = Node(6)
# # # # node_three = Node(7)
# # # # node_one.next = node_two
# # # # node_two.next = node_three

# # # # # Input List: 5 -> 6 -> 7
# # # # print_linked_list(halve_list(node_one))

# # # class Node:
# # #     def __init__(self, value, next=None):
# # #         self.value = value
# # #         self.next = next

# # # # For testing
# # # def print_linked_list(head):
# # #     current = head
# # #     while current:
# # #         print(current.value, end=" -> " if current.next else "\n")
# # #         current = current.next

# # # def delete_tail(head):
# # #     # first check if empty 
# # #     if head is None: 
# # #         return None 
    
# # #     current = head
# # #     while current.next.next is not None: 
# # #         current = current.next 
        
# # #     current.next = None 
# # #     return head
    
# # # butterfly = Node("Common Butterfly")
# # # ladybug = Node("Ladybug")
# # # beetle = Node("Scarab Beetle")
# # # butterfly.next = ladybug
# # # ladybug.next = beetle

# # # # Input List: butterfly -> ladybug -> beetle
# # # print_linked_list(delete_tail(butterfly))


# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def find_min(head):
#     # pass in the head, then we will iterate through the list checking for lowest value 
#     current = head
#     smallest = current.value
#     while current:
#         if current.value < smallest:
#             smallest = current.value
#         current = current.next
#     return smallest
 


# head1 = Node(5, Node(6, Node(7, Node(8))))
# head2 = Node(8, Node(5, Node(6, Node(7))))
# # Linked List: 5 -> 6 -> 7 -> 8
# print(find_min(head1))

# # Linked List: 8 -> 5 -> 6 -> 7
# print(find_min(head2))



class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def delete_item(head, item):
    # take head, if the head i
    if head.value == item:
        return head.next
        
    current = head
    
    while current.next: 
        if current.next.value == item: 
            # checks if the next value will be removed 
            current.next = current.next.next #this will set the next value 
            return head
        current = current.next
    return head 
#works?

        


slingshot = Node("Slingshot")
peaches = Node("Peaches")
beetle = Node("Scarab Beetle")
slingshot.next = peaches
peaches.next = beetle

# Linked List: slingshot -> peaches -> beetle
print_linked_list(delete_item(slingshot, "Peaches"))

# Linked List: slingshot -> beetle
print_linked_list(delete_item(slingshot, "Triceratops Torso"))