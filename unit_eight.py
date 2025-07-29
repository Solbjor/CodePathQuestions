# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root
   
def count_odd_splits(root,counter):
    if not root:
        return True
    
    if not root.left and not root.right:
        # nothing leave as is
        pass
    elif root.left and root.right: 
        # nothing leave as is but we need to continue traversing
        pass
    else: 
        counter += 1
                 
    count_odd_splits(root.left, counter)
    count_odd_splits(root.right, counter)
    
    return counter


# Using build_tree() function included at top of page
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)
counter = 0
print(count_odd_splits(monstera, counter))
print(count_odd_splits(None, counter))


class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
            
         
def find_flower(inventory, name):
    if inventory.val == name: 
        return True
    else: 
        pass
    find_flower(inventory.left, name)
    find_flower(inventory.right, name)
    return False


values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 