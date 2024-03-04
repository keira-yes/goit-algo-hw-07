def search_min(root):
    if root is None:
        return None
    
    # Переміщення по лівому піддереву
    while root.left is not None:
        root = root.left
    
    if root.val is None:
        print("Дерево порожнє")
        return

    return root.val