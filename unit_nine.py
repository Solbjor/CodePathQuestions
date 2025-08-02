class TreeNode():
     def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right

        
def merge_orders(order1, order2):
   if not order1 and not order2: 
       return None 
   elif not order1: 
       return order2 
   elif not order2: 
       return order1 
   
   # create the merged tree
   merger = TreeNode(order1.val + order2.val)
   merger.left = merge_orders(order1.left, order2.left)
   merger.right = merge_orders(order1.right, order2.right)

   return merger



cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)


# Using print_tree() function included at top of page
print_tree(merge_orders(order1, order2))