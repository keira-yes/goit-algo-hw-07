from search_max import search_max

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

# Test
root = Node(5)
root = insert(root, 21)
root = insert(root, 7)
root = insert(root, 4)
root = insert(root, 34)
root = insert(root, 6)
root = insert(root, 8)

# Пошук максимального значення
search_max(root)
