class ListNode:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


        
def remove_duplicates(head):
    if not head:
        return None
        
    current = head
    while current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        current = current.next
    return head
    
def insert_method_1(head, val):
    temp = ListNode(val)
    if not head:
        return temp
        
    last = head
    while last.next is not None:
        last = last.next
        
    last.next = temp
    return head
    
def create_linked_list_from_array(values):
    head = None
    for val in values:
        head = insert_method_1(head, val)
            
    return head
        
        
