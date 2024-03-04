def search_max(root):
    if root is None:
        return None
    
    # Переміщення по правому піддереву
    while root.right is not None:
        root = root.right
    
    if root.val is not None:
        print(f"Найбільше значення у дереві: {root.val}")
    else:
        print("Дерево порожнє")
        
    return root.val