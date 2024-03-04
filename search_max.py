def search_max(root):
    if root is None:
        return None
    
    # Переміщення по правому піддереву
    while root.right is not None:
        root = root.right
    
    if root.val is None:
        print("Дерево порожнє")
        return
        
    return root.val